# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.core import serializers
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from library.models import *
from library.parser import *
from platform import node
import os
import uuid
from django.core.context_processors import csrf


@login_required
def book_import(request):
    if node().upper() == "LENOVO":
        path = "/home/nikitos/Downloads/S.T.A.L.K.E.R__[rutracker.org]/"
    else:
        path = "c:\\Downloads\\S.T.A.L.K.E.R__[rutracker.org]\\fb2\\"
    files = find_files_by_mask(path, ".fb2")

    a = []
    for book in parse_files(files):
        if 'Authors' in book.keys():
            for author in book['Authors']:
                if not (
                Author.objects.filter(firstname=author['author_first_name'], lastname=author['author_last_name'])):
                    Author(lastname=author['author_last_name'], firstname=author['author_first_name']).save()
                    a += [author]

                    # print(book['Genre'][0])



                    Book(book_name=book['title'],
                         book_md5=book['md5'],
                         # book_annotation=book['Annotation'],

                         book_genre=BookGenre.objects.get(pk=book['Genre'][0])).save()
                # # print()

                print(book['Genre'][0])
                print(BookGenre.objects.get(pk=book['Genre'][0]))

    return render_to_response("library/import.html", {'import_data': a})


def author_search(request):
    pass

@login_required
def osinfo(request):
    return render_to_response("library/osinfo.html", {'osinfo': {'sysname': os.uname()[0],
                                                                 'nodename': os.uname()[1],
                                                                 'release': os.uname()[2],
                                                                 'version': os.uname()[3],
                                                                 'machine': os.uname()[4]}})


def createuser(request):
    try:
        u = User.objects.create_superuser(username='nikitos', email='xx@xx.ru', password="admin4all")
        u.save()
        return render_to_response("library/result_message.html")
    except Exception as E:
        return render_to_response("library/result_message.html", {'error_message': {'error_message': str(E)}})


@login_required
def delete(request):
    try:
        Author.objects.all().delete()
        return render_to_response("library/result_message.html")
    except Exception as E:
        return render_to_response("library/result_message.html", {'error_message': {'error_message': str(E)}})


@login_required
def index(request):
    return render_to_response("library/index.html", {'user': request.user})


@login_required
def testemail(request):
    from django.core.mail import EmailMessage
    email = EmailMessage('Hello', """
    Email from django
    reset password link
    %s
    """ % (uuid.uuid4()), to=['nikitachukov@me.com'])

    email.send()


def testck(request):
    args = {}
    args.update(csrf(request))
    return render_to_response("library/ckeditortest.html", args)


@login_required
def downloadgenres(request):
    with open("file.json", "w") as out:
        data = serializers.serialize("xml", BookGenre.objects.all())
        out.write(data)
    fp = open('file.json', 'rb')
    response = HttpResponse(FileWrapper(fp), content_type=' application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=genres.xml'
    return response



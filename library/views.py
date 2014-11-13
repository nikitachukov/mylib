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
        if 'title' in book.keys():
            title = book['title']
        if 'md5' in book.keys():
            md5 = book['md5']
        if 'Annotation' in book.keys():
            annotation = book['Annotation']


        if 'Genre' in book.keys():
            genre = BookGenre.objects.get(pk=book['Genre'][0])

        Book(book_name=title,
             book_md5=md5,
             book_annotation=annotation,
             book_genre=genre).save()

        Book.book_author.add(Author.objects.get_or_create(firstname=firstname, lastname=lastname))


        if 'Authors' in book.keys():
            for author in book['Authors']:
                firstname = author['author_first_name']
                lastname = author['author_last_name']
                # BookAuthor = Author.objects.filter(firstname=firstname, lastname=lastname)
                #
                # if not BookAuthor:
                #     BookAuthor = Author(firstname=firstname, lastname=lastname).save()


                # BA=Author.objects.get_or_create(firstname=firstname, lastname=lastname)
                # if Book:
                #     if Author:
                    # Book.book_author.add(Author.objects.get_or_create(firstname=firstname, lastname=lastname))

                        # ba=BookAuthor(author=Author.objects.get_or_create(firstname=firstname, lastname=lastname),book=Book)
                        # ba.save()

                    # Book.save()
                #     print(BookAuthor)


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
        Book.objects.all().delete()
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



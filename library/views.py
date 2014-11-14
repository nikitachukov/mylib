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
        path = "c:\\Downloads\\S.T.A.L.K.E.R__[rutracker.org]\\fb2+++\\"
    files = find_files_by_mask(path, ".fb2")

    a = []
    for file in parse_files(files):

        if 'filename' in file.keys():
            filename = file['filename']

        if 'title' in file.keys():
            title = file['title']
        if 'md5' in file.keys():
            md5 = file['md5']
        if 'Annotation' in file.keys():
            annotation = file['Annotation']

        if 'Genre' in file.keys():
            genre = BookGenre.objects.filter(pk=file['Genre'][0])
            if genre:
                genre = genre[0]
            else:
                genre = BookGenre.objects.get(pk='no_genre')

        book = Book.objects.create(book_name=title,
                                   book_file_name=filename,
             book_md5=md5,
             book_annotation=annotation,
             book_genre=genre)
        book.save()
        print(book)

        if 'Authors' in file.keys():
            for AAauthor in file['Authors']:
                author = Author.objects.get_or_create(firstname=AAauthor['author_first_name'],
                                                      lastname=AAauthor['author_last_name'])
                # print(author[0])
                book.book_author.through.objects.create(author=author[0], book=book)


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


@login_required
def testlink(request):
    book = Book.objects.get(book_md5='BE3B3E2B29A2C0DEEAB923336A763CE4')
    author = Author.objects.get(firstname='Владимир', lastname='Величко')
    print(book)
    book.book_author.through.objects.create(author=author, book=book[0])

    # print(author)
    # book.book_author.add(author)
    # book.save()

    # BookAuthor.objects.create(book=book,author=author)
    # print(BookAuthor)
    # BookAuthor.save()
    print(book)
    print(author)



    # Book.objects.create_book("Pride and Prejudice")
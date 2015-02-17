# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.core import serializers
from django.core.servers.basehttp import FileWrapper
from library.models import *
from library.fb2_parser0 import *
from time import time,sleep
from platform import node
import os
import uuid
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import django
from pprint import pprint
import platform
import json
from django.http import HttpResponse

@login_required
def BookList(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render_to_response("library/books_old.html", {'books': books})



@login_required
def Books(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render_to_response("library/books.html", {'books': books})


@login_required
def book_import(request):

    start=time()

    Books=[]
    Doubles=[]
    Errors=[]


    files = find_files_by_mask(settings.BOOKS_LOCATION, ".fb2")

    a = []

    Books,Doubles,Errors=parse_files(files)
    for file in Books:

        if 'filename' in file.keys():
            filename = file['filename']

        if 'title' in file.keys():
            title = file['title']
        if 'md5' in file.keys():
            md5 = file['md5']
        if 'Annotation' in file.keys():
            annotation = file['Annotation']

        if 'cover_file_name' in file.keys():
            cover_file_name = file['cover_file_name']
            cover_image ='covers/'+os.path.basename(file['cover_file_name'])
            # print(cover_image)
        else:
            cover_file_name = None
            cover_image = None

        if 'Genre' in file.keys():
            genre = BookGenre.objects.filter(pk=file['Genre'][0])
            if genre:
                genre = genre[0]
            else:
                genre = BookGenre.objects.get(pk='no_genre')

        book = Book.objects.create(book_name=title,
                                   # book_file_name_original=filename,
             book_md5=md5,
             book_annotation=annotation,
             book_genre=genre,
             # cover_file_name=cover_file_name,
             cover=cover_image
        )

        a.append(book)

        book.save()



        if 'Authors' in file.keys():
            for AAauthor in file['Authors']:
                author = Author.objects.get_or_create(firstname=AAauthor['author_first_name'],
                                                      lastname=AAauthor['author_last_name'])[0]

                book.book_author.through.objects.create(author=author, book=book)
    #

    return render_to_response("library/import.html", {'import_data': a, 'time': time()-start})


def author_search(request):
    pass

@login_required
def osinfo(request):
        return render_to_response("library/osinfo.html", {'osinfo': {
                                                                 'nodename': platform.node(),
                                                                 'version': platform.python_implementation()+platform.python_version(),
                                                                 'arch':platform.system()+' '+platform.version()+' '+platform.architecture()[0],
                                                                 'processor':platform.processor(),
                                                                 'django':'Django '+django.get_version()}})


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
def testemail(request):
    from django.core.mail import EmailMessage
    email = EmailMessage('Hello', """
    Email from django
    reset password link
    %s
    """ % (uuid.uuid4()), to=['nikitachukov@me.com'])

    email.send()


@login_required
def downloadgenres(request):
    with open("file.json", "w") as out:
        data = serializers.serialize("xml", BookGenre.objects.all())
        out.write(data)
    fp = open('file.json', 'rb')
    response = HttpResponse(FileWrapper(fp), content_type=' application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=stations.xml'
    return response



@login_required
def iphone_location(request):
    from django.conf import settings
    print(settings.ICLOUD_USER)
    print(settings.ICLOUD_PASSWORD)


    from pyicloud import PyiCloudService
    api = PyiCloudService(settings.ICLOUD_USER, settings.ICLOUD_PASSWORD)
    for index, item in enumerate(api.devices):
        if item.status()['name']=='Iphone_nikitos':
            location=item.location()

            pprint(location)

            return render_to_response("library/map.html",
                              {'location':
                                   {'latitude': str(location['latitude']),
                                    'longitude': str(location['longitude']),
                                    'horizontalAccuracy':str(location['horizontalAccuracy'])

                                    }})
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from library.models import *
from library.parser import *
import platform
import os


def book_import(request):
    if platform.node().upper() == "LENOVO":
        path = "/home/nikitos/Downloads/S.T.A.L.K.E.R__[rutracker.org]/"
    else:
        path = "c:\\Downloads\\S.T.A.L.K.E.R__[rutracker.org]"
    files = find_files_by_mask(path, ".fb2")
    a = []
    for book in parse_files(files):
        if 'Authors' in book.keys():
            for author in book['Authors']:
                firstname = author['author_first_name']
                lastname = author['author_last_name']
                if not (Author.objects.filter(firstname=firstname, lastname=lastname)):
                    dbauthor = Author(lastname=author['author_last_name'],
                                      firstname=author['author_first_name']
                    )
                    dbauthor.save()

                    a += [author]

    return render_to_response("library/import.html", {'import_data': a})


def author_search(request):
    pass


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


def delete(request):
    try:
        Author.objects.all().delete()
        return render_to_response("library/result_message.html")
    except Exception as E:
        return render_to_response("library/result_message.html", {'error_message': {'error_message': str(E)}})


@login_required()
def index(request):
    # return render(request, "library/index.html")
    return render_to_response("library/index.html")


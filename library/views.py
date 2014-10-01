# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from library.models import *
from library.parser import *
import os


def book_import(request):
    print(os.uname()[1].upper())
    if os.uname()[1].upper() == "LENOVO":
        path = "/home/nikitos/Downloads/S.T.A.L.K.E.R__[rutracker.org]/"
    else:
        path = "c:\\Downloads\\S.T.A.L.K.E.R__[rutracker.org]"
    # book=Book(book_name = "Test",book_annotation="xxx")
    # book.save()

    files = find_files_by_mask(path, ".fb2")

    print(files)

    a = []
    for book in parse_files(files):
        if 'Authors' in book.keys():
            a += book['Authors']
            if book['Authors'][0]['author_first_name']:

                # if not len(Author.objects.filter(author_idx=book['Autors'][0]['author_first_name'].upper()+book['Autors'][0]['author_last_name'].upper())):
                if True:
                    author = Author(lastname=book['Authors'][0]['author_last_name'],
                                    firstname=book['Authors'][0]['author_first_name']
                    )
                    author.save()

    return render(request, "library/import.html", {'import_data': a})


def author_search(request):
    # print (os.uname().)
    pass


def osinfo(request):
    return render(request, "library/osinfo.html", {'osinfo': {'sysname': os.uname()[0],
                                                              'nodename': os.uname()[1],
                                                              'release': os.uname()[2],
                                                              'version': os.uname()[3],
                                                              'machine': os.uname()[4]}})

def createuser(request):
    try:
        u = User.objects.create_superuser(username='nikitos_zxzz',email='xx@xx.ru',password="admin4all")
        u.save()
        return render(request,"library/error_message.html")
    except Exception as E:
        ErrorMessage={'error_message':str(E)}
        return render(request,"library/error_message.html",{'error_message':ErrorMessage})


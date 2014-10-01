# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from library.models import *
from library.parser import *

def book_import(request):
    # book=Book(book_name = "Test",book_annotation="xxx")
    # book.save()

    files = find_files_by_mask("c:\\Downloads\\S.T.A.L.K.E.R__[rutracker.org]", ".fb2")
    # print(parse_files(files))
    a = []
    for book in parse_files(files):
        if 'Autors' in book.keys():
            a+=book['Autors']
            if book['Autors'][0]['author_first_name']:

                # if not len(Author.objects.filter(author_idx=book['Autors'][0]['author_first_name'].upper()+book['Autors'][0]['author_last_name'].upper())):
                if True:


                    author = Author(lastname=book['Autors'][0]['author_last_name'],
                                    firstname=book['Autors'][0]['author_first_name']
                    )
                    author.save()


    return render(request,"library/import.html",{'import_data':a})

def author_search(request):
    pass

    # print(len(Author.objects.filter(
    #     author_idx="ВЯЧЕСЛАВШАЛЫГИН")))
    # return render(request,"library/import.html")


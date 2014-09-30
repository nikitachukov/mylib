# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from library.models import *
def book_import(request):
    book=Book(book_name = "Test",book_annotation="xxx")
    book.save()
    return render(request,"library/import.html",)


# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from library.models import Author, Book


class AuthorInline(admin.TabularInline):
    model = Book.book_author.through


class BookAdmin(admin.ModelAdmin):
    fields = ['book_name', 'book_annotation', 'book_date', 'book_url']
    list_filter = ['book_name', 'book_author', 'book_date']
    inlines = [AuthorInline, ]


class AuthorAdmin(admin.ModelAdmin):
    fields = ['firstname', 'lastname']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
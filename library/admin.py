# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from library.models import Author, Book, BookGenre


class AuthorInline(admin.TabularInline):
    model = Book.book_author.through


class BookAdmin(admin.ModelAdmin):
    fields = ['book_name', 'book_annotation', 'book_md5']
    list_filter = ['book_name', 'book_author']
    inlines = [AuthorInline, ]


class AuthorAdmin(admin.ModelAdmin):
    fields = ['firstname', 'lastname']


class BookGenreAdmin(admin.ModelAdmin):
    fields = ['genre_code', 'genre_name']


admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
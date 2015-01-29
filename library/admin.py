# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from library.models import Author, Book, BookGenre


class AuthorInline(admin.TabularInline):
    model = Book.book_author.through


class BookAdmin(admin.ModelAdmin):
    fields = ['book_name', 'book_genre', 'book_annotation', 'book_file_name_original', 'book_md5', 'cover_file_name',
              'cover_image']
    ordering = ('book_name',)
    search_fields = ('book_name', 'book_file_name_original', 'book_md5',)
    list_filter = ['book_name', 'book_genre', 'book_author']
    inlines = [AuthorInline, ]


class AuthorAdmin(admin.ModelAdmin):
    ordering = ('lastname', 'firstname',)
    fields = ['lastname', 'firstname']


class BookGenreAdmin(admin.ModelAdmin):
    ordering = ('genre_name',)
    fields = ['genre_code', 'genre_name']


admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)

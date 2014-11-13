# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.views import generic


class Post(models.Model):
    content = RichTextField()


class Author(models.Model):
    class Meta():
        db_table = 'authors'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True)


class Book(models.Model):
    class Meta():
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.book_name

    book_name = models.CharField(max_length=200, verbose_name='Название книги')
    book_annotation = models.TextField(verbose_name='Аннотация к книги')
    book_date = models.DateTimeField(auto_now_add=True)
    book_url = models.URLField(blank=True)
    book_likes = models.IntegerField(default=0)
    book_author = models.ManyToManyField(Author, through='BookAuthor', verbose_name='Авторы книги', null=True)
    book_md5 = models.CharField(max_length=32)


class BookAuthor(models.Model):
    book = models.ForeignKey(Author)
    author = models.ForeignKey(Book)


class BookGenre(models.Model):
    class Meta():
        # db_table = 'books'
        verbose_name = 'Жанр книги'
        verbose_name_plural = 'Жанры книги'

    def __str__(self):
        return self.genre_name

    genre_code = models.CharField(max_length=20, primary_key=True)
    genre_name = models.CharField(max_length=100)


# -*- coding: utf-8 -*-
from django.db import models


class Author(models.Model):
    class Meta():
        db_table = 'authors'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True)


class BookGenre(models.Model):
    class Meta():
        # db_table = 'books'
        verbose_name = 'Жанр книги'
        verbose_name_plural = 'Жанры книги'

    def __str__(self):
        return self.genre_name

    genre_code = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='Код жанра')
    genre_name = models.CharField(max_length=100, verbose_name='Описание жанра')


class Book(models.Model):
    class Meta():
        db_table = 'library_books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.book_name

    book_name = models.CharField(max_length=200, verbose_name='Название книги')
    book_annotation = models.TextField(verbose_name='Аннотация к книги', blank=True)
    book_date = models.DateTimeField(auto_now_add=True)
    book_url = models.URLField(blank=True)
    book_likes = models.IntegerField(default=0)
    book_author = models.ManyToManyField(Author, through='BookAuthor', verbose_name='Авторы книги', null=True)
    book_md5 = models.CharField(max_length=32)
    book_genre = models.ForeignKey(BookGenre)
    cover = models.ImageField(upload_to='covers/', blank=True)


class BookAuthor(models.Model):
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)





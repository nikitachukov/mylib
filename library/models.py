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
    lastname = models.CharField(max_length=100,blank=True)


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
    book_author = models.ManyToManyField(Author, through='BookAuthor', verbose_name='Авторы книги',null=True)



class BookAuthor(models.Model):
    book = models.ForeignKey(Author)
    author = models.ForeignKey(Book)

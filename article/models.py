# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = "article"

    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'

    article_title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    article_text = models.TextField(verbose_name='Текст статьи')
    article_date = models.DateTimeField(verbose_name='Дата статьи')
    article_likes = models.IntegerField(default=0, verbose_name='Лайки')


class Comments(models.Model):
    class Meta():
        db_table = "comments"

    verbose_name = 'Коментарии'
    comments_text = models.TextField(verbose_name='Комментарий')
    comments_article = models.ForeignKey(Article)


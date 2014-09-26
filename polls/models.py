# -*- coding: utf-8 -*-

# Create your models here.

from django.db import models


class Poll(models.Model):
    class Meta():
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.question

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    class Meta():
        db_table = 'choices'
        verbose_name = 'ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.choice_text

    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
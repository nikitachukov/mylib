# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0006_auto_20141114_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ManyToManyField(through='library.BookAuthor', to='library.Author', blank=True, null=True,
                                         verbose_name='Авторы книги'),
        ),
    ]

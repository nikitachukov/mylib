# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0002_auto_20141113_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_file_name',
            field=models.CharField(max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(null=True, to='library.BookGenre', blank=True),
        ),
    ]

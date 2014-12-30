# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0005_auto_20141114_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='author',
            field=models.ForeignKey(to='library.Author'),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(to='library.Book'),
        ),
    ]

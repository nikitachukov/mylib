# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0004_auto_20141114_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_md5',
            field=models.CharField(max_length=32),
        ),
    ]

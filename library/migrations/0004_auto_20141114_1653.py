# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0003_auto_20141114_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_md5',
            field=models.CharField(editable=False, max_length=32),
        ),
    ]

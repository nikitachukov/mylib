# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'authors',
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('book_name', models.CharField(verbose_name='Название книги', max_length=200)),
                ('book_annotation', models.TextField(verbose_name='Аннотация к книги')),
                ('book_date', models.DateTimeField(auto_now_add=True)),
                ('book_url', models.URLField(blank=True)),
                ('book_likes', models.IntegerField(default=0)),
                ('book_md5', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'books',
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('author', models.ForeignKey(to='library.Book')),
                ('book', models.ForeignKey(to='library.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('genre_code', models.CharField(unique=True, serialize=False, verbose_name='Код жанра', max_length=20,
                                                primary_key=True)),
                ('genre_name', models.CharField(verbose_name='Описание жанра', max_length=100)),
            ],
            options={
                'verbose_name': 'Жанр книги',
                'verbose_name_plural': 'Жанры книги',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.ManyToManyField(through='library.BookAuthor', null=True, verbose_name='Авторы книги',
                                         to='library.Author'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(to='library.BookGenre'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from django.contrib import admin
from article.models import Article, Comments


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = [('article_title', 'article_date'), 'article_text']
    inlines = [ArticleInline]
    list_filter = ['article_date']


admin.site.register(Article, ArticleAdmin)

# Register your models here.

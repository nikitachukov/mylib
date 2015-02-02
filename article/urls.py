#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nikitos'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^all/$', 'article.views.articles',name='articles'),
                       url(r'^get/(?P<article_id>\d+)/$', 'article.views.article', name='article'),
                       url(r'^addlike/(?P<article_id>\d+)/$', 'article.views.addlike', name='addlike'),
                       url(r'^addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment',name='addcomment'),
                       url(r'^', 'article.views.articles'),
)
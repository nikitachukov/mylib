# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns('',
                       url(r'^import/$', views.book_import, name='book_import'),
                       )
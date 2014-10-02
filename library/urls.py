# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns('',
                       url(r'^import/$', views.book_import, name='book_import'),
                       url(r'^delete/$', views.delete, name='book_delte'),
                       url(r'^search/$', views.author_search, name='author_search'),
                       url(r'^osinfo/$', views.osinfo, name='osinfo'),
                       url(r'^createuser/$', views.createuser, name='createuser'),
                       )
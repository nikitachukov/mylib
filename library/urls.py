# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns('',
                       url(r'^books/$', views.BookList, name='books'),
                       url(r'^import/$', views.book_import, name='book_import'),
                       url(r'^delete/$', views.delete, name='book_delte'),
                       url(r'^list/$', views.BookList, name='book_list'),
                       url(r'^search/$', views.author_search, name='author_search'),
                       url(r'^osinfo/$', views.osinfo, name='osinfo'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^createuser/$', views.createuser, name='createuser'),
                       url(r'^testemail/$', views.testemail, name='testemail'),
                       url(r'^downloadgenres/$', views.downloadgenres, name='downloadgenres'),
                       url(r'^map/$', views.iphone_location, name='iphone_location'),
)
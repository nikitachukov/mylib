# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns('',
                       url(r'^books/$', views.books, name='books'),
                       url(r'^book/(?P<book_id>\d+)/$', views.book, name='book'),
                       url(r'^addtolist/(?P<book_id>\d+)/$', views.addtolist, name='addtolist'),

                       url(r'^books_old/$', views.BookList, name='books_old'),
                       url(r'^import/$', views.book_import, name='book_import'),
                       url(r'^delete/$', views.delete, name='book_delte'),
                       url(r'^list/$', views.BookList, name='book_list'),
                       url(r'^search/$', views.author_search, name='author_search'),
                       url(r'^osinfo/$', views.osinfo, name='osinfo'),

                       url(r'^createuser/$', views.createuser, name='createuser'),
                       url(r'^testemail/$', views.testemail, name='testemail'),
                       url(r'^downloadgenres/$', views.downloadgenres, name='downloadgenres'),
                       url(r'^map/$', views.iphone_location, name='iphone_location'),

)
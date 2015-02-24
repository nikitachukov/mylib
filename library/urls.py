# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns('',
                       url(r'^books/$', views.books, name='books'),
                       url(r'^book/(?P<book_id>\d+)/$', views.book, name='book'),
                       url(r'^addtolist/(?P<book_id>\d+)/$', views.addtolist, name='addtolist'),
                       url(r'^import/$', views.book_import, name='book_import'),
                       url(r'^delete/$', views.delete, name='book_delte'),
                       url(r'^downloadgenres/$', views.downloadgenres, name='downloadgenres'),

)
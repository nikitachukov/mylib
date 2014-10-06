# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from authsys import views

urlpatterns = patterns('',
                       url(r'^login/$', views.login, name='login'),
                       url(r'^logout/$', views.logout, name='logout'),
)
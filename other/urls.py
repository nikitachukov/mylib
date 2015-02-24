# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from other import views

urlpatterns = patterns('',
                       url(r'^osinfo/$', views.osinfo, name='osinfo'),
                       url(r'^findiphone/$', views.iphone_location, name='iphone_location')
)
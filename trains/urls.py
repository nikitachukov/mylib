# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from trains import views

urlpatterns = patterns('',
                       url(r'^stations/$', views.stations_list_ajax, name='resetpassword'),
)
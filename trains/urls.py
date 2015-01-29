# -*- coding: utf-8 -*-
__author__ = 'nikitos'

from django.conf.urls import patterns, url

from trains import views

urlpatterns = patterns('',
                       url(r'^stations/$', views.stations_list_ajax, name='stations_list_ajax'),
                       url(r'^stations_my/$', views.stations_list_ajax_my, name='stations_list_ajax_my'),
)
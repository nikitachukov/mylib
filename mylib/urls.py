# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^polls/', include('polls.urls',namespace="polls")),
                       url(r'^library/', include('library.urls',namespace="library")),

                       url(r'^auth/', include('authsys.urls', namespace="authsys")),

                       url(r'^$', lambda x: HttpResponseRedirect('/library/index')),


)

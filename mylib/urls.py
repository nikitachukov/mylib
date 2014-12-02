# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^library/', include('library.urls', namespace="library")),

                       url(r'^auth/', include('account.urls', namespace="account")),

                       url(r'^$', lambda x: HttpResponseRedirect('/library/index')),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),




)

# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.conf import settings


from mylib import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^library/', include('library.urls', namespace="library")),
                       url(r'^articles/', include('article.urls', namespace="articles")),
                       url(r'^other/', include('other.urls', namespace="other")),
                       url(r'^trains/', include('trains.urls', namespace="trains")),
                       url(r'^auth/', include('account.urls', namespace="account")),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,
                                                                                  'show_indexes': True}),
)

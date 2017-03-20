# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sections.views import contact

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', auth_views.logout),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^contact_form', contact),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA

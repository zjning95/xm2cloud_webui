#! -*- coding: utf-8 -*-


from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include


from . import views


urlpatterns = [
    url(r'^cmp/', include('xm2cloud_cmp.urls', namespace='xm2cloud_cmp')),
    url(r'^web/', include('xm2cloud_web.urls', namespace='xm2cloud_web')),
    url(r'^blog/', include('xm2cloud_blog.urls', namespace='xm2cloud_blog')),
    url(r'^accounts/', include('xm2cloud_auth.urls', namespace='xm2cloud_auth')),
    url(r'^terminal/', include('xm2cloud_term.urls', namespace='xm2cloud_term')),

    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='xm2cloud_media')
    ]

urlpatterns += [
    url(r'', views.HttpNotFoundView.as_view(), name='http_not_found'),
]

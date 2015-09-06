from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^settings/', 'my_admin.views.admin_settings'),
)

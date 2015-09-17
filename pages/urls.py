from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<categ_url>[\-\w]+)/$', 'pages.views.pages_view'),
    url(r'^(?P<categ_url>[\-\w]+)/(?P<url>[\-\w]+)/$', 'pages.views.page_in_categ_view'),
]

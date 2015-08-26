from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<url>[\-\w]+)/$', 'pages.views.page_view'),
]

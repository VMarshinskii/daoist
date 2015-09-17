from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^create_phone_order_view/$', 'communication.views.create_phone_order_view'),
    url(r'^add_subscriber_view/$', 'communication.views.add_subscriber_view'),
]

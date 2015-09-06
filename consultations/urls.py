from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'consultations.views.consultations_view'),
    url(r'^(?P<consultation_id>\d+)/$', 'consultations.views.consultation_view'),
]

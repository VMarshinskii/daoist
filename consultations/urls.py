from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'consultations.views.consultations_view'),
    url(r'^ask/$', 'consultations.views.consultation_ask_view'),
    url(r'^thanks/$', 'consultations.views.consultation_ask_thanks_view'),
    url(r'^(?P<url>[\-\w]+)/$', 'consultations.views.consultation_view'),
]

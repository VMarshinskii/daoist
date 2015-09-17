from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'pages.views.home_view'),
    url(r'^admin/', include('my_admin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^consultations/', include('consultations.urls')),
    url(r'^about/$', 'pages.views.about_view'),
    url(r'^contacts/$', 'pages.views.contacts_view'),
    url(r'^reviews/$', 'communication.views.reviews_view'),
    url(r'^reviews/create/$', 'communication.views.review_create'),
    url(r'^reviews/thanks/$', 'communication.views.review_thanks'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^communication/', include('communication.urls')),
    url(r'^', include('pages.urls')),
]

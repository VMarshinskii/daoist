from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'blog.views.home_view', name='home'),
    url(r'^admin/', include('my_admin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^consultations/', include('consultations.urls')),
    url(r'^about/$', 'pages.views.about_view'),
    url(r'^contacts/$', 'pages.views.contacts_view'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^', include('pages.urls')),
]

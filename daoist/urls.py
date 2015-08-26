from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'daoist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'blog.views.home_view', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^', include('pages.urls')),
]

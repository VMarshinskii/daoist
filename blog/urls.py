from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'blog.views.home_view'),
    url(r'^(?P<url>[\-\w]+)/$', 'blog.views.post_view'),
]

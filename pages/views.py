from django.shortcuts import render_to_response, Http404
from models import Page
from my_admin.models import SiteSettings


def page_view(request, url):
    try:
        page = Page.objects.get(url=url, public=True)
        return render_to_response("page.html", {'page': page})
    except Page.DoesNotExist:
        raise Http404()


def about_view(request):
    try:
        settings = SiteSettings.objects.get(id=1)
        return render_to_response("about.html", {'settings': settings})
    except SiteSettings.DoesNotExist:
        raise Http404()

def contacts_view(request):
    try:
        settings = SiteSettings.objects.get(id=1)
        return render_to_response("contacts.html", {'settings': settings})
    except SiteSettings.DoesNotExist:
        raise Http404()
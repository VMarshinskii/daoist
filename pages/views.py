from django.shortcuts import render_to_response, Http404, HttpResponse
from models import Page, CATEGORIES_CHOICES
from my_admin.models import SiteSettings


def home_view(request):
    return render_to_response("home.html")


def pages_view(request, categ_url):
    for choice in CATEGORIES_CHOICES:
        if categ_url in choice:
            pages = Page.objects.filter(category=categ_url, public=True)
            return render_to_response("pages.html", {'posts': pages})
    return Http404()


def page_in_categ_view(request, categ_url, url):
    try:
        page = Page.objects.get(url=url, public=True, category=categ_url)
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
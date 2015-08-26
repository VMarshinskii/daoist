from django.shortcuts import render_to_response, Http404
from models import Page


def page_view(request, url):
    try:
        page = Page.objects.get(url=url, public=True)
        return render_to_response("page.html", {'page': page})
    except Page.DoesNotExist:
        raise Http404

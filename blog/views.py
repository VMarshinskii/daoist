from django.shortcuts import render_to_response, Http404
from models import Post


def home_view(request):
    posts = Post.objects.filter(public=True)
    return render_to_response("home.html", {'posts': posts})

def post_view(request, url):
    try:
        post = Post.objects.get(url=url, public=True)
        return render_to_response("post.html", {'post': post})
    except Post.DoesNotExist:
        raise Http404

# -*- coding: utf-8 -*-
from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('templatetags/right_news.html')
def right_news():
    posts = Post.objects.filter(public=True)[:5]
    return {'posts': posts}
from django import template
from my_admin.models import SiteSettings
register = template.Library()

@register.inclusion_tag('templatetags/header_block.html')
def header_block():
    settings = SiteSettings.objects.get(id=1)
    return {'settings': settings}
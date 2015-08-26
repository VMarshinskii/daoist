from django.contrib import admin
from models import Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Page, PageAdmin)

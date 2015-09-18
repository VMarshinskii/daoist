from django.contrib import admin
from models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_link', 'public')
    search_fields = ['title']
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Post, PostAdmin)

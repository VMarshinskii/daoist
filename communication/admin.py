from django.contrib import admin
from models import PhoneOrder, Subscriber, Reviews


class PhoneOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'get_date_time', 'viewed')
    search_fields = ['name', 'phone']
    list_filter = ['viewed']


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'get_date_time')
    search_fields = ['name', 'email']


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profession', 'age', 'get_date_time', 'public')
    search_fields = ['name', 'profession']
    list_filter = ['public']


admin.site.register(PhoneOrder, PhoneOrderAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Reviews, ReviewsAdmin)

from django.contrib import admin
from consultations.models import Consultation, ConsultationAsk


class ConsultationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}


class ConsultationAskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profession', 'age', 'get_date_time', 'viewed')
    search_fields = ['name', 'profession']
    list_filter = ['viewed']


admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(ConsultationAsk, ConsultationAskAdmin)


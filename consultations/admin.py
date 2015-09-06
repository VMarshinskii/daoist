from django.contrib import admin
from consultations.models import Consultation

class ConsultationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

admin.site.register(Consultation, ConsultationAdmin)


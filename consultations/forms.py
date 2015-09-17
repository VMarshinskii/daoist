from django import forms
from models import ConsultationAsk


class ConsultationAskForm(forms.ModelForm):
    class Meta:
        model = ConsultationAsk
        fields = ['name', 'profession', 'age', 'email', 'text']

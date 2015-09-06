from django.shortcuts import render_to_response, Http404
from models import Consultation


def consultations_view(request):
    consultations = Consultation.objects.filter(public=True)
    return render_to_response("consultations.html", {'consultations': consultations})

def consultation_view(request, consultation_id):
    try:
        consultation = Consultation.objects.get(id=consultation_id, public=True)
        return render_to_response("consultation.html", {'consultation': consultation})
    except Consultation.DoesNotExist:
        raise Http404()

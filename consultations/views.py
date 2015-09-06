from django.shortcuts import render_to_response, Http404
from models import Consultation


def consultations_view(request):
    consultations = Consultation.objects.filter(public=True)
    return render_to_response("consultations.html", {'consultations': consultations})

def consultation_view(request, url):
    try:
        consultation = Consultation.objects.get(url=url, public=True)
        return render_to_response("consultation.html", {'consultation': consultation})
    except Consultation.DoesNotExist:
        raise Http404()

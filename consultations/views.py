from django.shortcuts import render_to_response, Http404, redirect
from django.template.context_processors import csrf
from models import Consultation
from forms import ConsultationAskForm


def consultations_view(request):
    consultations = Consultation.objects.filter(public=True)
    return render_to_response("consultations.html", {'consultations': consultations})


def consultation_view(request, url):
    try:
        consultation = Consultation.objects.get(url=url, public=True)
        return render_to_response("consultation.html", {'consultation': consultation})
    except Consultation.DoesNotExist:
        raise Http404()


def consultation_ask_view(request):
    args = {'form': ConsultationAskForm()}
    args.update(csrf(request))
    if request.POST:
        reviews_form = ConsultationAskForm(request.POST)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('/consultations/thanks/')
        args['form'] = reviews_form
    return render_to_response("consultation_ask_create.html", args)


def consultation_ask_thanks_view(request):
    return render_to_response("consultation_ask_thanks.html")

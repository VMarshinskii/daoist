# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse, Http404, render_to_response, redirect
from communication.forms import ReviewsForm
from django.template.context_processors import csrf
from models import PhoneOrder, Subscriber, Reviews
from StringIO import StringIO
import simplejson as json
from pyunisend import PyUniSend


def create_phone_order_view(request):
    if request.GET:
        response = {'errors': 0}

        name = request.GET.get('name', '')
        if name == '':
            response['errors'] = 1
            response['name_error'] = "Введите имя"

        phone = request.GET.get('phone', '')
        if phone == '':
            response['errors'] = 1
            response['phone_error'] = "Введите телефон"

        if response['errors'] == 0:
            phone_order = PhoneOrder(name=name, phone=phone)
            phone_order.save()

        return HttpResponse(json.dumps(response))

    raise Http404()


def add_subscriber_view(request):
    if request.GET:
        response = {'errors': 0}

        name = request.GET.get('name', '')
        if name == '':
            response['errors'] = 1
            response['name_error'] = "Введите имя"

        email = request.GET.get('email', '')
        if email == '':
            response['errors'] = 1
            response['email_error'] = "Введите e-mail"
        else:
            try:
                Subscriber.objects.get(email=email)
                response['errors'] = 1
                response['email_error'] = "Такой e-mail уже подписан"
            except Subscriber.DoesNotExist:
                pass

        if response['errors'] == 0:
            subscriber = Subscriber(name=name, email=email)
            subscriber.save()

            api = PyUniSend('5wy7awr4cunj36qds3e565bi4xi5wmzy57kzw9wo')
            # 5715758, 5715742
            result = api.subscribe(list_ids='5715758', fields={
                'email': subscriber.email,
                'Name': subscriber.name.encode("UTF-8")
            }, double_optin=1)

            print result

        return HttpResponse(json.dumps(response))

    raise Http404()


def reviews_view(request):
    reviews = Reviews.objects.filter(public=True)
    return render_to_response("reviews.html", {'reviews': reviews})


def review_create(request):
    args = {'reviews_form': ReviewsForm()}
    args.update(csrf(request))
    if request.POST:
        reviews_form = ReviewsForm(request.POST)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('/reviews/thanks/')
        args['reviews_form'] = reviews_form
    return render_to_response("review_create.html", args)


def review_thanks(request):
    return render_to_response("review_thanks.html")

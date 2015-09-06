# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, Http404, redirect
from django.template.context_processors import csrf
from models import SiteSettings
from forms import SiteSettingsForm



def admin_settings(request):
    if request.user.is_authenticated():
        args = {}
        args.update(csrf(request))
        try:
            model = SiteSettings.objects.get(id=1)
            args['form'] = SiteSettingsForm(instance=model)
        except SiteSettings.DoesNotExist:
            args['form'] = SiteSettingsForm()

        if request.POST:
            form = SiteSettingsForm(request.POST, request.FILES)
            if form.is_valid():
                model = form.save(commit=False)
                model.id = 1
                model.save()
                return redirect('/admin/')
            else:
                args['form'] = form

        return render_to_response("settings.html", args)
    else:
        return redirect('/admin/')
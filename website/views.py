import datetime
from random import randint

from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Contacts, Gallery, Docs, News, UsefuleInfo, SubmissionsElectricity, LandPlot, WaterMeter, WaterSubmission
from .forms import WaterSubmissionForm


def index(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    context = {"contact": contact, "main_image": f"/static/src/image{randint(1, 13)}.jpg"}
    return render(request, "website/index.html", context)


def contacts(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    contacts_list = Contacts.objects.order_by("-job")
    context = {"contacts_list": contacts_list, "contact": contact, "main_image": f"/static/src/image{randint(1, 13)}.jpg"}
    return render(request, "website/contacts.html", context)


def docs(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    docs_list = Docs.objects.order_by("-date")
    context = {"docs_list": docs_list, "contact": contact, "main_image": f"/static/src/image{randint(1, 13)}.jpg"}
    return render(request, "website/docs.html", context)


def galery(request) -> HttpResponse:
    #TODO
    contact = Contacts.objects.order_by("-job")[0]
    context = {"contact": contact, "main_image": f"/static/src/image{randint(1, 13)}.jpg"}
    return render(request, "website/galery.html", context)


def login(request) -> HttpResponse:
    #TODO
    contact = Contacts.objects.order_by("-job")[0]
    context = {"contact": contact}
    return render(request, "website/login.html", context)

    
def news(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    news_list = News.objects.order_by("-date")
    context = {"news_list": news_list, "contact": contact, "main_image": f"/static/src/image{randint(1, 13)}.jpg"}
    return render(request, "website/news.html", context)

    
def submissions(request) -> HttpResponse:
    #TODO
    contact = Contacts.objects.order_by("-job")[0]
    context = {"contact": contact, "main_image": f"/static/src/image{randint(1, 13)}.jpg"}
    return render(request, "website/submissions.html", context)

    
def usefullinfo(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    usefulInfo_list = UsefuleInfo.objects.order_by("-index")
    context = {"usefulInfo_list": usefulInfo_list, "contact": contact, "main_image": f"/static/src/image{randint(1, 13)}.jpg"}
    return render(request, "website/usefullinfo.html", context)


@login_required
def water_meters(request):
    land_plots = dict()
    for land_plot in LandPlot.objects.filter(user__id=request.user.id):
        water_meters = dict()
        for water_meter in land_plot.water_meters():
           water_meters[water_meter] = { 'form': WaterSubmissionForm(), 'last_submitted_value': water_meter.water_submissions().last() }
        land_plots[land_plot] = water_meters

    context = {'land_plots': land_plots}
    return render(request, "website/water_meters.html", context)


@login_required
def water_submissions(request, water_meter_id):
    current_water_meter = get_object_or_404(WaterMeter, land_plot__user__id=request.user.id, id=water_meter_id)
    current_form = WaterSubmissionForm(request.POST, water_meter = current_water_meter)

    water_submission = WaterSubmission()
    
    if current_form.is_valid():
        water_submission.value = current_form.cleaned_data['value']
        water_submission.water_meter = current_water_meter
        water_submission.created_at = datetime.datetime.now()
        water_submission.save()
        return HttpResponseRedirect(reverse('water_meters'))
    
    land_plots = dict()
    for land_plot in LandPlot.objects.filter(user__id=request.user.id):
        water_meters = dict()
        for water_meter in land_plot.water_meters():
           form = current_form if current_water_meter == water_meter else WaterSubmissionForm()
           water_meters[water_meter] = { 'form': form, 'last_submitted_value': water_meter.water_submissions().last() }
        land_plots[land_plot] = water_meters

    context = {'land_plots': land_plots}
    return render(request, "website/water_meters.html", context)

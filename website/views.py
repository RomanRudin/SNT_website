from django.http.response import HttpResponse
from random import randint
from django.shortcuts import render

from .models import Contacts, Gallery, Docs, News, UsefuleInfo, SubmissionsElectricity, SubmissionsWater



def index(request) -> HttpResponse:
    return render(request, "website/main.html", context={"main_image": f"/static/src/image{randint(1, 13)}.jpg"})

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
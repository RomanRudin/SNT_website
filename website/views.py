from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Contacts, Gallery, Docs, News, UsefuleInfo, SubmissionsElectricity, SubmissionsWater



def index(request) -> HttpResponse:
    return render(request, "main/index.html")

def contacts(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    contacts_list = Contacts.objects.order_by("-job")
    context = {"contacts_list": contacts_list, "contact": contact}
    return render(request, "main/contacts.html", context)


def docs(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    docs_list = Docs.objects.order_by("-date")
    context = {"docs_list": docs_list, "contact": contact}
    return render(request, "main/docs.html", context)


def galery(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    context = {"contact": contact}
    return render(request, "main/galery.html", context)


def login(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    context = {"contact": contact}
    return render(request, "main/login.html", context)

    
def news(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    news_list = News.objects.order_by("-date")
    context = {"news_list": news_list, "contact": contact}
    return render(request, "main/news.html", context)

    
def submissions(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    context = {"contact": contact}
    return render(request, "main/submissions.html", context)

    
def usefulinfo(request) -> HttpResponse:
    contact = Contacts.objects.order_by("-job")[0]
    usefulInfo_list = UsefuleInfo.objects.order_by("-index")
    context = {"usefulInfo_list": usefulInfo_list, "contact": contact}
    return render(request, "main/usefulinfo.html", context)
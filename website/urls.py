from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path("docs/", views.docs, name="docs"),
    path("galery/", views.galery, name="galery"),
    path("login/", views.login, name="login"),
    path("news/", views.news, name="news"),
    path("submissions/", views.submissions, name="submissions"),
    path("usefulinfo/", views.usefulinfo, name="usefulinfo"),
]

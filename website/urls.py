from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path("", views.index, name="main"),
    path("contacts/", views.contacts, name="contacts"),
    path("docs/", views.docs, name="docs"),
    path("galery/", views.galery, name="galery"),
    path("login/", views.login, name="login"),
    path("news/", views.news, name="news"),
    path("submissions/", views.submissions, name="submissions"),
    path("usefullinfo/", views.usefullinfo, name="usefullinfo"),
]

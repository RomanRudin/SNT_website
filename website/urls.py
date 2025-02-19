from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("submissions/", views.submissions, name="submissions"),
    path("usefullinfo/", views.usefullinfo, name="usefullinfo"),
]

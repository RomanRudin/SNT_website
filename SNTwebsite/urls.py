'''
URL configuration for SNTwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
from django.contrib import admin
from django.urls import path, include

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('docs/', views.docs, name='docs'),
    path('galery/', views.galery, name='galery'),
    path('news/', views.news, name='news'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('water-meters/', views.water_meters, name='water_meters'),
    path('water-meters/<int:water_meter_id>/water-submissions', views.water_submissions, name='water_submissions'),

    path('admin/', admin.site.urls),
]

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import bank_form,change_mobile
urlpatterns = [
    path('',bank_form),
    path('change_mobile/',change_mobile)
]
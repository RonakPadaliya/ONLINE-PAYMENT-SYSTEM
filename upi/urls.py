from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import upi_form
app_name="upi"
urlpatterns = [
    url('',upi_form,name="upi_form")
]

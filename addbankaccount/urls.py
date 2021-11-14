from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import bank_form
app_name='addbankaccount'
urlpatterns = [
    url('',bank_form,name="bank_form"),
 ]
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import change_bank_account,change_mobile,change_upi
app_name='change'
urlpatterns = [
    url('mobile/',change_mobile,name="change_mobile"),
    url('bankaccount/',change_bank_account,name="change_bank_account"),
    url('upi/',change_upi,name="change_upi"),
]
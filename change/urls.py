from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import change_bank_account,change_mobile,change_upi,remove_bank_account,block_bank_account,bank_account_unblock
app_name='change'
urlpatterns = [
    url('mobile/',change_mobile,name="change_mobile"),
    url('bankaccount/',change_bank_account,name="change_bank_account"),
    url('upi/',change_upi,name="change_upi"),
    url('remove_bank_account/',remove_bank_account,name="remove_bank_account"),
    url('block_bank_account/',block_bank_account,name="block_bank_account"),
    url('bank_account_unblock/',bank_account_unblock,name="bank_account_unblock"),
]
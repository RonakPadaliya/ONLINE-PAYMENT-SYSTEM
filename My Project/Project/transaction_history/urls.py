from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import history
app_name='transaction_history'
urlpatterns = [
    url(r'history/',history,name="history")
]
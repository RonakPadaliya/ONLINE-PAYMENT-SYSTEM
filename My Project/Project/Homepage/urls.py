from django.conf.urls import url
from django.urls import path, include
from .views import homepage

urlpatterns = [
    url(r'$', homepage),
]
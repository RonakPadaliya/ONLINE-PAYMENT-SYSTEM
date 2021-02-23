import django
from django.conf.urls import url
from django.urls import include
from .views import login, registration, welcome

urlpatterns = [
    url(r'^$', login),
    url(r'registration/', registration),
    url(r'welcome/', welcome),
]
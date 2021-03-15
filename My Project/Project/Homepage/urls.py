from django.conf.urls import url
from django.urls import path, include
from .views import homepage

app_name="Homepage"
urlpatterns = [
    url(r'^$', homepage,name="homepage"),
]
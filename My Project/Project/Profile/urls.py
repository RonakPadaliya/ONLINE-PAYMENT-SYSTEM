import django
from django.conf.urls import url
from django.urls import include
from .views import profile
app_name='Profile'

urlpatterns = [
    url(r'profile/', profile,name="profile"),
]
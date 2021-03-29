import django
from django.conf.urls import url
from django.urls import include
from .views import logout,login, registration, welcome, forgot, guidelines
app_name='Login'

urlpatterns = [
    url(r'^$', login,name="login"),
    url(r'registration/', registration,name="registration"),
    url(r'welcome/', welcome,name="welcome"),
    url(r'logout/', logout,name="logout"),
    url(r'forgot/', forgot,name="forgot"),
    url(r'guidelines/', guidelines,name="guidelines"),
]
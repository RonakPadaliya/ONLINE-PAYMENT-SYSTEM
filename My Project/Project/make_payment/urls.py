import django
from django.conf.urls import url
from django.urls import include
from .views import payment_method,acno,mobile_no
app_name='make_payment'

urlpatterns = [
    url(r'payment_method',payment_method,name="payment_method"),
    url(r'acno/',acno,name="acno"),
    url(r'mobile_no/',mobile_no,name="mobile_no")
]
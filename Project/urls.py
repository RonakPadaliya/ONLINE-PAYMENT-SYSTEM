"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path(r'admin', admin.site.urls),
    url(r'^', include("Homepage.urls")),
    url(r'^Login', include("Login.urls")),
    url(r'^addbankaccount',include("addbankaccount.urls")),
    url(r'^upi', include("upi.urls")),
    url(r'^change',include("change.urls")),
    url(r'^make_payment',include("make_payment.urls")),
    url(r'^transaction_history',include("transaction_history.urls")),
    url(r'^Profile',include("Profile.urls")),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

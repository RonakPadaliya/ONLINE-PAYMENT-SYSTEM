from django.shortcuts import render

# Create your views here.
def addbankaccount(request):
    return render(request,"addbankaccount/base.html")
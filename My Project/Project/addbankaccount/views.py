from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import Bank
# Create your views here.
from Login.models import Users_info
from django.db import connection

# def home(request):
#     return render(request,'addbankaccount/bank_details.html')
# def check(request):
#     mobile = request.POST['mobile']
#     p = Users_info.objects.raw(f'select * from login_users_info where mobile={mobile}')
#     q = Bank.objects.raw(f'select * from addbankaccount_bank where mobile={mobile}')
#     print(len(list(p)))
#     print(len(list(q)))
#     if len(list(p)) == 0:
#         messages.info(request, "you have to change your mobile number")
#         return render(request, 'addbankacccount/bank_details.html')
#     else:
#         return redirect('/check')
def bank_form(request):
    if request.method=="POST":
        mobile=request.POST['mobile']
        acno=request.POST['acno']

        p = Users_info.objects.raw(f'SELECT * FROM login_users_info where mobile={mobile}')
        q = Bank.objects.raw(f'SELECT * FROM addbankaccount_bank where mobile={mobile}')
        print(len(list(p)))
        print(len(list(q)))
        if len(list(p)) == 0:
            messages.info(request, "you have to change your mobile number")
            return render(request, 'addbankaccount/bank_details.html')
        else:
            if len(list(q)) == 0:
                messages.info(request, "Your mobile number is not Linked with Bank")
                return render(request, 'addbankaccount/bank_details.html')
            else:
                messages.info(request, "successful")
                return render(request, 'addbankaccount/bank_details.html')
    else:
        return render(request,'addbankaccount/bank_details.html')

def change_mobile(request):
    if request.method =="post":
        print("abc")
    else:
        return render(request,'addbankaccount/change_mobile.html')

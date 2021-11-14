from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import Bank
from Login.models import Users_info
from django.db import connection


def bank_form(request):
    if request.method=="POST":
        mobile=request.POST['mobile']
        acno=request.POST['acno']
        check=request.session['user_username']
        if mobile == Users_info.objects.filter(username=check).first().mobile:
            if Bank.objects.filter(acno=acno).exists():
                if mobile == Bank.objects.filter(acno=acno).first().mobile:
                    if len(list(Bank.objects.raw(f'SELECT * FROM addbankaccount_bank where mobile={mobile}')))==1:
                        b = Bank.objects.filter(acno=acno).first()
                        b.status=1
                        u = Users_info.objects.filter(username=check).first()
                        u.status=1
                        b.username = Users_info.objects.get(username =check)
                        u.save()
                        b.save()
                        request.session['user_status']=1
                        request.session['bank_status']=1
                        request.session['bank_balance']=b.balance
                        #request.session['bank_block']=b.block
                        messages.success(request,"Sucessfully connected")
                        return redirect('http://127.0.0.1:8000/upi')
                    else:
                        messages.error(request,"Your mobile nummber is linked with mutiple account")
                        return render(request,'addbankaccount/bank_details.html')
                else:
                    messages.error(request,"Your mobile number is not linked with Bank")
                    return render(request,"addbankaccount/bank_details.html")
            else:
                messages.error(request,"Invalid account number")
                return render(request,"addbankaccount/bank_details.html")
        else:
            messages.error(request,"You have to change your mobile number")
            return render(request,"addbankaccount/bank_details.html")
    else:
        return render(request,"addbankaccount/bank_details.html")

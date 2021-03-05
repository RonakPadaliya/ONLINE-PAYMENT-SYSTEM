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
        check=request.session['username']
        if mobile == Users_info.objects.filter(username=check).first().mobile:
            if Bank.objects.filter(acno=acno).exists():
                if mobile == Bank.objects.filter(acno=acno).first().mobile:
                    b=Bank.objects.filter(acno=acno).first()
                    b.status=1
                    b.save()
                    u=Users_info.objects.filter(username=check).first()
                    u.status=1
                    u.save()
                    request.session['status']=1
                    request.session['add_bank_account']=True
                    messages.info(request,"Sucessfully connected")
                    return redirect('http://127.0.0.1:8000/Login/welcome')
                else:
                    messages.info(request,"Your mobile number is not linked with Bank")
                    return render(request,"addbankaccount/bank_details.html")
            else:
                messages.info(request,"Invalid account number")
                return render(request,"addbankaccount/bank_details.html")
        else:
            messages.info(request,"You have to change your mobile no")
            return render(request,"addbankaccount/bank_details.html")
    else:
        return render(request,"addbankaccount/bank_details.html")

def change_mobile(request):
    if request.method == "POST":
        oldmobile=request.POST['oldmobile']
        newmobile=request.POST['newmobile']
        check_username=request.session['username']
        if oldmobile == Users_info.objects.filter(username=check_username).first().mobile:
            if Users_info.objects.filter(mobile=newmobile).exists():
                messages.info(request,"Already Mobile NO is taken")
                return render(request,'addbankaccount/change_mobile.html')
            else:
                u =Users_info.objects.filter(username=check_username).first()
                u.mobile = newmobile
                u.save()
                messages.info(request,"successfully changed")
                return redirect('http://127.0.0.1:8000/Login/welcome')
        else:
            messages.info(request,"Wrong MobileNo")
            return render(request,"addbankaccount/change_mobile.html")
    else:
        return render(request,"addbankaccount/change_mobile.html")


def change_bankaccount(request):
    if request.session.get('add_bank_account') is not None:
        if request.method=="POST":
            mobile=request.POST['mobile']
            acno=request.POST['acno']
            check=request.session['username']
            if mobile == Users_info.objects.filter(username=check).first().mobile:
                if Bank.objects.filter(acno=acno).exists():
                    if mobile == Bank.objects.filter(acno=acno).first().mobile:
                        b=Bank.objects.filter(acno=acno).first()
                        b.status=1
                        b.save()
                        u=Users_info.objects.filter(username=check).first()
                        u.status=1
                        u.save()
                        request.session['status']=1
                        messages.info(request,"Sucessfully connected")
                        return redirect('http://127.0.0.1:8000/Login/welcome')
                    else:
                        messages.info(request,"Your mobile number is not linked with Bank")
                        return render(request,"addbankaccount/change_bankaccount.html")
                else:
                    messages.info(request,"Invalid account number")
                    return render(request,"addbankaccount/change_bankaccount.html")
            else:
                messages.info(request,"You have to change your mobile no")
                return render(request,"addbankaccount/change_bankaccount.html")
        else:
            return render(request,"addbankaccount/change_bankaccount.html")
    else:
        messages.info(request,"you need to first add bank account")
        return render(request,'addbankaccount/bank_details.html')

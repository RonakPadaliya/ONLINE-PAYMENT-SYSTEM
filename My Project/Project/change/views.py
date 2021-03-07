from django.shortcuts import render,redirect
from Login.models import Users_info
from addbankaccount.models import Bank
from django.contrib import messages
# Create your views here.

def change_mobile(request):
    if request.method == "POST":
        oldmobile=request.POST['oldmobile']
        newmobile=request.POST['newmobile']
        check_username=request.session['user_username']
        if oldmobile == Users_info.objects.filter(username=check_username).first().mobile:
            if Users_info.objects.filter(mobile=newmobile).exists():
                messages.info(request,"Already Mobile NO is taken")
                return render(request,'change/change_mobile.html')
            else:
                u =Users_info.objects.filter(username=check_username).first()
                u.mobile = newmobile
                u.save()
                messages.info(request,"successfully changed")
                return redirect('http://127.0.0.1:8000/Login/welcome')
        else:
            messages.info(request,"Wrong MobileNo")
            return render(request,"change/change_mobile.html")
    else:
        return render(request,"change/change_mobile.html")


def change_bank_account(request):
    print(request.session['user_status'])
    if request.session.get('user_status') != 0:
        if request.method=="POST":
            mobile=request.POST['mobile']
            acno=request.POST['acno']
            check=request.session['user_username']
            if mobile == Users_info.objects.filter(username=check).first().mobile:
                if Bank.objects.filter(acno=acno).exists():
                    if mobile == Bank.objects.filter(acno=acno).first().mobile:
                        b=Bank.objects.filter(acno=acno).first()
                        b.status=1
                        u=Users_info.objects.filter(username=check).first()
                        u.status=1
                        oldac=request.session['bank_acno']
                        oldac_obj=Bank.objects.filter(acno=oldac).first()
                        oldac_obj.username=None
                        b.username=Users_info.objects.get(username=check)
                        u.save()
                        b.save()
                        request.session['status']=1
                        messages.info(request,"Sucessfully connected")
                        return redirect('http://127.0.0.1:8000/Login/welcome')
                    else:
                        messages.info(request,"Your mobile number is not linked with Bank")
                        return render(request,"change/change_bank_account.html")
                else:
                    messages.info(request,"Invalid account number")
                    return render(request,"change/change_bank_account.html")
            else:
                messages.info(request,"You have to change your mobile no")
                return render(request,"change/change_bank_account.html")
        else:
            return render(request,"change/change_bank_account.html")
    else:
        messages.info(request,"you need to first add bank account")
        return render(request,'change/change_bank_account_not_add_bank_account.html')


def change_upi(request):
    if request.session['user_upi_staus'] == 1:
        if request.method =="post":
            username = request.POST['username']
            password = request.POST['password']
            oldpin = request.POST['oldpin']
            newpin = request.POST['newpin']

            if username == request.session['user_username']:
                if password == request.session['user_password']:
                    if oldpin == request.session['user_upi']:
                        u=Users_info.objects.filter(username=username).first()
                        u.upi=newpin
                        request.session['user_upi']=newpin
                        u.save()
                        messages.info(request,"successfully changed")
                        return redirect(request,'../Login/welcome')
                    else:
                        messages.info(request,"Invalid PIN")
                        return render(request,'change/change_upi.html')
                else:
                    messages.info(request,"Invalid password")
                    return render(request,'change/change_upi.html')
            else:
                messages.info(request,"Invalid username")
                return render(request,'change/change_upi.html')
        else:
            return render(request,'change/change_upi.html')
    elif request.session['user_status'] == 0:
        return render(request,'change/change_upi_not_add_bank_account.html')
    elif request.session['user_upi_staus'] == 0:
        return render(request,"change/change_upi_not_create_upi.html")
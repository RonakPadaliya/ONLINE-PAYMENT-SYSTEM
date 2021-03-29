from django.shortcuts import render, redirect
from Login.models import Users_info
from addbankaccount.models import Bank
from django.contrib import messages
from make_payment.models import Transaction
#import Login.templates.Login
# Create your views here.

def profile(request):
    if request.method == "POST":
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        check=request.session['user_username']
        p=Users_info.objects.filter(username=check).first()
        p.first_name=fname
        p.last_name=lname
        p.email=email
        p.save()
        request.session['user_fname']=fname
        request.session['user_lname']=lname
        request.session['user_email']=email
        u=Bank.objects.filter(username=check).first()
        return render(request,'Profile/base.html',{'u':u})        
    else:
        check=request.session['user_username']
        u=Bank.objects.filter(username=check).first()
        return render(request,'Profile/base.html',{'u':u})

def deleteAccount(request):
    if request.method=="POST":
        username=request.POST['username']
        mobile=request.POST['mobile']
        password=request.POST['password']
        uname=request.session['user_username']
        if username == uname:
            u=Users_info.objects.filter(username=uname).first()
            if mobile == u.mobile:
                if password == u.password:
                    if request.session.get("user_status") is not None:
                        ac=Bank.objects.filter(username=uname).first().acno
                        b=Bank.objects.filter(acno=ac).first()
                        b.username=None
                        b.status=None
                        b.save()

                    #if u.status is not None:
                    #    del request.session['bank_block']
                    u.delete()
                    while Transaction.objects.filter(sender_username=uname).first() is not None:
                        t=Transaction.objects.filter(sender_username=uname).first()
                        t.delete()
                    del request.session['user_username']
                    del request.session['user_password']
                    del request.session['user_mobile']
                    del request.session['user_status']
                    del request.session['user_upi']
                    del request.session['user_upi_staus']
                    del request.session['user_email']
                    
                    messages.info(request,"Successfully deleted")
                    return redirect('../Login')
                else:
                    messages.error(request,"Password is Invalid !")
                    return render(request,'Profile/deleteAccount.html')
            else:
                messages.error(request,"Mobile Number is Invalid !")
                return render(request,'Profile/deleteAccount.html')
        else:
            messages.error(request,"Username is Invalid !")
            return render(request,'Profile/deleteAccount.html')
    else:
        return render(request,'Profile/deleteAccount.html')
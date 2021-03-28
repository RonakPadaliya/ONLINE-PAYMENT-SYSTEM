from django.shortcuts import render
from Login.models import Users_info
from addbankaccount.models import Bank
from django.contrib import messages
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
            if mobile == Users_info.objects.filter(username=uname).first().mobile:
                if password == Users_info.objects.filter(username=uname).first().password:
                    u=Users_info.objects.filter(username=uname).first()
                    b=Bank.objects.filter(username=uname).first()
                    u.delete()
                    b.username=None
                    b.status=None
                    messages.info(request,"Successfully deleted")
                    return render(request,'Login/login.html')
                else:
                     return render(request,'Profile/deleteAccount.html')
            else:
                 return render(request,'Profile/deleteAccount.html')
        else:
             return render(request,'Profile/deleteAccount.html')
    else:
        return render(request,'Profile/deleteAccount.html')
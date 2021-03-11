from django.shortcuts import render
from Login.models import Users_info
from addbankaccount.models import Bank
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
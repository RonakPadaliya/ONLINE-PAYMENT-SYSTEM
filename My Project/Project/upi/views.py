from django.shortcuts import render,redirect
from addbankaccount.models import Bank
from Login.models import Users_info
from django.contrib import messages
# Create your views here.
def upi_form(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        acno = request.POST['acno']
        username = request.POST['username']
        password = request.POST['password']
        upi=request.POST['upi']
        user_check = request.session['username']
        acno=int(acno)
        if username == user_check:
            if password == Users_info.objects.filter(username=user_check).first().password:
                if mobile == Bank.objects.filter(username=user_check).first().mobile:
                    if acno == Bank.objects.filter(username=user_check).first().acno:
                        u=Users_info.objects.filter(username=user_check).first()
                        request.session['upi']=upi
                        u.upi_staus = 1
                        u.upi=upi
                        u.save()
                        messages.success(request,"Successfully Created")
                        return redirect('../Login/welcome')
                    else:
                        messages.error(request,"AC NO is invalid")
                        return render(request,'upi/upi_form.html')
                else:
                    messages.error(request,"Mobile NO is invalid")
                    return render(request,'upi/upi_form.html')
            else:
                messages.error(request,"password is invalid")
                return render(request,'upi/upi_form.html')
        else:
            messages.error(request,"Username is invalid")
            return render(request,'upi/upi_form.html')
    else:
        return render(request,'upi/upi_form.html')
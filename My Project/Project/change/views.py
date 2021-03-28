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
                messages.error(request,"Already Mobile Number is taken")
                return render(request,'change/change_mobile.html')
            else:
                u =Users_info.objects.filter(username=check_username).first()
                u.mobile=newmobile
                u.save()
                messages.success(request,"successfully changed")
                return redirect('http://127.0.0.1:8000/Login/welcome')
        else:
            messages.error(request,"Wrong MobileNo")
            return render(request,"change/change_mobile.html")
    else:
        return render(request,"change/change_mobile.html")


def change_bank_account(request):
    if request.session.get('user_status') is not None:
        if request.session.get('bank_block') is None:
            if request.method=="POST":
                mobile=request.POST['mobile']
                oldacno=request.POST['oldacno']
                newacno=request.POST['newacno']
                check=request.session['user_username']
                if mobile == Users_info.objects.filter(username=check).first().mobile:
                    if Bank.objects.filter(acno=newacno).exists():
                        if mobile == Bank.objects.filter(acno=newacno).first().mobile:
                            if len(list(Bank.objects.raw(f'SELECT * FROM addbankaccount_bank where mobile={mobile}'))) == 1:
                                b=Bank.objects.filter(acno=newacno).first()
                                oldac=Bank.objects.filter(acno=oldacno).first()
                                oldac.username=None
                                oldac.status=None
                                b.username=Users_info.objects.get(username=check)
                                b.status=1
                                b.save()
                                oldac.save()
                                u=Users_info.objects.filter(username=check).first()
                                u.upi=None
                                u.upi_staus=None
                                request.session['user_status']=1
                                request.session['bank_status']=1
                                request.session['bank_balance']=b.balance
                                request.session['user_upi_staus']=None
                                u.save()
                                messages.success(request,"Sucessfully connected")
                                return redirect('http://127.0.0.1:8000/upi')
                            else:
                                messages.error(request, "Your mobile no is linked with mutiple account")
                                return render(request, 'addbankaccount/bank_details.html')
                        else:
                            messages.error(request,"Your mobile number is not linked with Bank")
                            return render(request,"change/change_bank_account.html")
                    else:
                        messages.error(request,"Invalid account number")
                        return render(request,"change/change_bank_account.html")
                else:
                    messages.error(request,"You have to change your mobile no")
                    return render(request,"change/change_bank_account.html")
            else:
                return render(request,"change/change_bank_account.html")
        else:
            return render(request,"change/change_bank_account_allready_block.html")
    else:
        return render(request,'change/change_bank_account_not_add_bank_account.html')


def change_upi(request):
    if request.session['user_upi_staus'] is not None:
        if request.session['bank_block'] is None:
            if request.method == "POST" :
                username = request.POST['username']
                password = request.POST['password']
                oldpin = request.POST['oldpin']
                newpin = request.POST['newpin']
                check=request.session['user_username']
                oldpin=int(oldpin)
                request.session['user_upi']=int(request.session['user_upi'])
                if username == check:
                    if password == Users_info.objects.filter(username=check).first().password:
                        if oldpin == int(Users_info.objects.filter(username=check).first().upi):
                            u=Users_info.objects.filter(username=username).first()
                            u.upi=newpin
                            u.save()
                            request.session['user_upi']=newpin
                            messages.success(request,"successfully changed")
                            return render(request,'Login/welcome.html')
                        else:
                            messages.error(request,"Invalid PIN")
                            return render(request,'change/change_upi.html')
                    else:
                        messages.error(request,"Invalid password")
                        return render(request,'change/change_upi.html')
                else:
                    messages.error(request,"Invalid username")
                    return render(request,'change/change_upi.html')
            else:
                return render(request,'change/change_upi.html')
        else:
            return render(request,'change/change_upi_allready_block.html')
    elif request.session['user_status'] is None:
            return render(request,'change/change_upi_not_add_bank_account.html')
    elif request.session['user_upi_staus'] is None:
        return render(request,"change/change_upi_not_create_upi.html")

def remove_bank_account(request):
    if request.session.get('user_status') is not None:
        if request.session.get('bank_block') is None:
            if request.method=="POST":
                mobile=request.POST['mobile']
                acno=request.POST['acno']
                password=request.POST['password']
                acno=int(acno)
                check_username=request.session['user_username']
                if mobile == Users_info.objects.filter(username=check_username).first().mobile:
                    if acno == Bank.objects.filter(acno=acno).first().acno:
                        if password == Users_info.objects.filter(username=check_username).first().password:
                            b = Bank.objects.filter(acno=acno).first()
                            b.username=None
                            b.status=None
                            u = Users_info.objects.filter(username=check_username).first()
                            u.status=None
                            u.upi=None
                            u.upi_staus=None
                            b.save()
                            u.save()
                            request.session['user_upi']=None
                            request.session['user_upi_staus']=None
                            request.session['user_status']=None
                            messages.success(request,"Successsfully Bank account removed")
                            return render(request,"Login/welcome.html")
                        else:
                            messages.error(request,"Password is Incorrect")
                            return render(request,"change/remove_bank_account.html")
                    else:
                        messages.error(request,"Account number is invalid")
                        return render(request,"change/remove_bank_account.html")
                else:
                    messages.error(request,"Mobile number is Invalid")
                    return render(request,"change/remove_bank_account.html")
            else:
                return render(request,"change/remove_bank_account.html")
        else:
            return render(request,"change/remove_bank_account_allready_block.html")
    else:
        return render(request,'change/remove_bank_account_not_add_bank_account.html')

def block_bank_account(request):
    if request.session.get('user_status') is not None:
        if request.session.get('bank_block') is None:
            if request.method=="POST":
                mobile=request.POST['mobile']
                acno=request.POST['acno']
                password=request.POST['password']
                acno=int(acno)
                check_username=request.session['user_username']
                if mobile == Users_info.objects.filter(username=check_username).first().mobile:
                    if acno == Bank.objects.filter(acno=acno).first().acno:
                        if password == Users_info.objects.filter(username=check_username).first().password:
                            b = Bank.objects.filter(acno=acno).first()
                            b.block=1
                            b.save()
                            request.session['bank_block']=1
                            messages.success(request,"Successsfully Bank account Blocked")
                            return render(request,"Login/welcome.html")
                        else:
                            messages.error(request,"Password is Incorrect")
                            return render(request,"change/block_bank_account.html")
                    else:
                        messages.error(request,"Account number is invalid")
                        return render(request,"change/block_bank_account.html")
                else:
                    messages.error(request,"Mobile number is Invalid")
                    return render(request,"change/block_bank_account.html")
            else:
                return render(request,"change/block_bank_account.html")
        else:
            return render(request,"change/block_bank_account_allready_block.html")
    else:
        return render(request,'change/block_bank_account_not_add_bank_account.html')

def bank_account_unblock(request):
    if request.session.get('user_status') is not None:
        if request.session.get('bank_block') is not None:
            if request.method=="POST":
                mobile=request.POST['mobile']
                acno=request.POST['acno']
                password=request.POST['password']
                acno=int(acno)
                check_username=request.session['user_username']
                if mobile == Users_info.objects.filter(username=check_username).first().mobile:
                    if acno == Bank.objects.filter(acno=acno).first().acno:
                        if password == Users_info.objects.filter(username=check_username).first().password:
                            b = Bank.objects.filter(acno=acno).first()
                            b.block=None
                            b.save()
                            request.session['bank_block']=None
                            messages.success(request,"Successsfully Bank account Unblocked")
                            return render(request,"Login/welcome.html")
                        else:
                            messages.error(request,"Password is Incorrect")
                            return render(request,"change/bank_account_unblock.html")
                    else:
                        messages.error(request,"Account number is invalid")
                        return render(request,"change/bank_account_unblock.html")
                else:
                    messages.error(request,"Mobile number is Invalid")
                    return render(request,"change/bank_account_unblock.html")
            else:
                return render(request,"change/bank_account_unblock.html")
        else:
            return render(request,"change/bank_account_allready_unblock.html")
    else:
        return render(request,'change/bank_account_unblock_not_add_bank_account.html')
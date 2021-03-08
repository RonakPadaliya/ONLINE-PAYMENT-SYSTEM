from django.contrib import messages
from django.shortcuts import render,redirect
from Login.models import Users_info
from addbankaccount.models import Bank
from .models import Transaction
# Create your views here.
def payment_method(request):
    return render(request,'make_payment/payment_method.html')

def acno(request):
    if request.method == "POST":
        acno=request.POST['acno']
        amount=request.POST['amount']
        purpose=request.POST['purpose']
        receiver_ac_no=request.POST['receiver_ac_no']
        upi=request.POST['upi']
        username=request.session['user_username']
        acno=int(acno)
        receiver_ac_no=int(receiver_ac_no)
        upi=int(upi)
        amount=int(amount)
        if acno == Bank.objects.filter(username=username).first().acno:
            if receiver_ac_no == Bank.objects.filter(acno=receiver_ac_no).first().acno:
                if upi == Users_info.objects.filter(username=username).first().upi:
                    if amount < Bank.objects.filter(username=username).first().balance-100:
                        current_b=Bank.objects.filter(username=username).first()
                        current_b.balance=current_b.balance-amount
                        receiver_b=Bank.objects.filter(acno=receiver_ac_no).first()
                        receiver_b.balance=receiver_b.balance+amount
                        current_b.save()
                        receiver_b.save()
                        t=Transaction()
                        u=Users_info.objects.filter(username=username).first()
                        t.sender_name=u.first_name
                        t.sender_mobile=u.mobile
                        t.sender_acno=acno
                        t.sender_amount=amount
                        t.sender_purpose=purpose
                        t.sender_username=username
                        t.receiver_name=Bank.objects.filter(acno=receiver_ac_no).first().first_name
                        t.receiver_mobile=Bank.objects.filter(acno=receiver_ac_no).first().mobile
                        t.receiver_acno=receiver_ac_no
                        t.payment_type="acno"
                        t.save()
                        messages.success(request,"Successfully payment Done")
                        return redirect('http://127.0.0.1:8000/Login/welcome/')
                    else:
                        messages.error(request,"Your balance is too low")
                        return render(request,'make_payment/acno.html')
                else:
                    messages.error(request,"upi is invalid")
                    return render(request,'make_payment/acno.html')
            else:
                messages.error(request,"receiver ac no is invalid")
                return render(request,'make_payment/acno.html')
        else:
            messages.error(request,"your acno is invalid")
            return render(request,'make_payment/acno.html')
    else:
        return render(request,'make_payment/acno.html')


def mobile_no(request):
    if request.method == "POST":
        acno=request.POST['acno']
        amount=request.POST['amount']
        purpose=request.POST['purpose']
        receiver_mobile_no=request.POST['receiver_mobile_no']
        upi=request.POST['upi']
        username=request.session['user_username']
        acno=int(acno)
        receiver_ac_no=int(receiver_mobile_no)
        upi=int(upi)
        amount=int(amount)
        if acno == Bank.objects.filter(username=username).first().acno:
            if receiver_mobile_no == Bank.objects.filter(acno=receiver_ac_no).first().mobile:
                if Bank.objects.filter(acno=receiver_ac_no).first().username is not None:
                    if upi == Users_info.objects.filter(username=username).first().upi:
                        if amount < Bank.objects.filter(username=username).first().balance-100:
                            current_b = Bank.objects.filter(username=username).first()
                            current_b.balance = current_b.balance - amount
                            receiver_b = Bank.objects.filter(acno=receiver_ac_no).first()
                            receiver_b.balance = receiver_b.balance + amount
                            current_b.save()
                            receiver_b.save()
                            t = Transaction()
                            u = Users_info.objects.filter(username=username).first()
                            t.sender_name = u.first_name
                            t.sender_mobile = u.mobile
                            t.sender_acno = acno
                            t.sender_amount = amount
                            t.sender_purpose = purpose
                            t.sender_username=username
                            t.receiver_name = Bank.objects.filter(acno=receiver_ac_no).first().first_name
                            t.receiver_mobile = receiver_mobile_no
                            t.receiver_acno = Bank.objects.filter(mobile=receiver_mobile_no).first().acno
                            t.payment_type = "mobileno"
                            t.save()
                            messages.success(request, "Successfully payment Done")
                            return redirect('http://127.0.0.1:8000/Login/welcome/')
                        else:
                            messages.error(request, "Your balance is too low")
                            return render(request, 'make_payment/mobile_no.html')
                    else:
                        messages.error(request, "upi is invalid")
                        return render(request, 'make_payment/mobile_no.html')
            else:
                messages.error(request, "receiver mobile no is invalid")
                return render(request, 'make_payment/mobile_no.html')
        else:
            messages.error(request, "your acno is invalid")
            return render(request, 'make_payment/mobile_no.html')
    else:
        return render(request, 'make_payment/mobile_no.html')

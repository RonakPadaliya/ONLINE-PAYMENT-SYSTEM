from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Users_info


def login(request):
    if request.session.get('username') is None:
        return render(request, 'Login/login.html')
    else:
        return redirect('Login/welcome/')


def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        mobile=request.POST['mobile']
        # check the data is entered or not by the user
        if username != '' and password != '' and password2 != '' and email != '' and first_name != '' and last_name != '':
            # check password and repassword are same or not
            if password == password2:
                if Users_info.objects.filter(username=username).exists():
                    messages.info(request,"User is already Exists!!")
                    return render(request,'Login/registration.html')
                elif Users_info.objects.filter(email=email).exists():
                    messages.info(request,"Email is already Exists!!")
                    return render(request,'Login/registration.html')
                elif Users_info.objects.filter(mobile=mobile).exists():
                    messages.info(request,"Mobile NO is already Exists!!")
                    return render(request,'Login/registration.html')
                else:
                    u = Users_info(username=username, password=password, email=email, first_name=first_name,last_name=last_name, mobile=mobile)
                    u.save()
                    return redirect('/Login')
            # if passwords are not match then again render register pagr
            else:
                messages.info(request, "password does not match")
                return redirect('registration')
        else:
            messages.info(request, "please enter the data")
            messages.info(request, "all fields are must required")
            return render(request, 'Login/registration.html')
    else:
        return render(request, 'Login/registration.html')
def welcome(request):
    if request.session.get('user_username') is None:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            if Users_info.objects.filter(username=username).exists() and Users_info.objects.filter(username=username).first().password==password:
                u=Users_info.objects.filter(username=username).first()
                request.session['user_username'] = u.username
                request.session['user_password'] = u.password
                request.session['user_mobile'] = u.mobile
                request.session['user_status'] = u.status
                request.session['user_upi'] = u.upi
                request.session['user_upi_staus'] = u.upi_staus
                request.session['user_email'] = u.email
                # request.session['user_acno']=u.acno
                # request.session['user_balance']=u.balance
                p=u.status
                print(p)
                print(u.username)
                return render(request, 'Login/welcome.html', {"username": username,'status':p})
            else:
                messages.info(request,"Invalid username or password")
                return render(request,'Login/login.html')
        else:
            return render(request, 'Login/login.html')
    else:
        return render(request,'Login/welcome.html')
        
def logout(request):
    if 'user_username' in request.session:
        del request.session['user_username']
        del request.session['user_password']
        del request.session['user_mobile']
        del request.session['user_status']
        del request.session['user_upi']
        del request.session['user_upi_staus']
        del request.session['user_email']
        messages.info(request,"you are successfully logout")
        return render(request,'Login/login.html')
    else:
        return render(request,'Login/login.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Users_info


def login(request):
    return render(request, 'Login/login.html')


def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        mobileno=request.POST['mobileno']
        # check the data is entered or not by the user
        if username != '' and password1 != '' and password2 != '' and email != '' and first_name != '' and last_name != '':
            # check password and repassword are same or not
            if password1 == password2:
                if Users_info.objects.filter(username=username).exists():
                    messages.info(request,"User is already Exists!!")
                    return render(request,'Login/registration.html')
                elif Users_info.objects.filter(email=email).exists():
                    messages.info(request,"Email is already Exists!!")
                    return render(request,'Login/registration.html')
                else:
                    u = Users_info(username=username, password1=password1, email=email, first_name=first_name,last_name=last_name, mobileno=mobileno)
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
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # check user is register or not
        # u = Users_info.check(username=username, password=password)
        # # user is  register then value of user is not None
        # if u is None:
        #     # login access to user
        #     messages.info(request, "Invalid username or password")
        #     return redirect('/Login')
        # else:
        #     return render(request, 'Login/welcome.html')
        if Users_info.objects.filter(username=username).exists() and Users_info.objects.filter(password1=password).exists():
            request.session['username'] = username
            return render(request, 'Login/welcome.html', {"username": username})
        else:
            messages.info(request,"Invalid username or password")
            return render(request,'Login/login.html')
    else:
        return render(request, 'Login/login.html')


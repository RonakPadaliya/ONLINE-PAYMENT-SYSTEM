from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Users_info


def login(request):
    return render(request, 'Login/login.html')


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
                else:
                    u = Users_info(username=username, password=password, email=email, first_name=first_name,last_name=last_name, mobileno=mobileno)
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
        if Users_info.objects.filter(username=username).exists() and Users_info.objects.filter(username=username).first().password==password:
            request.session['username'] = username
            return render(request, 'Login/welcome.html', {"username": username})
        else:
            messages.info(request,"Invalid username or password")
            return render(request,'Login/login.html')
    else:
        return render(request, 'Login/login.html')


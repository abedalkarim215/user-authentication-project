from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate
from django.contrib import messages


def home(request) :
    context = {

    }
    return render(request,'user_auth/home.html',context)


def login_user(request):
    if request.method == "GET":
        return render(request, 'user_auth/login.html')

    elif request.method == "POST":
        user_username = request.POST['username']
        user_password = request.POST['password']
        user = authenticate(request, username=user_username, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "your username or password is incorrect , please try again")
            return redirect("login_user")

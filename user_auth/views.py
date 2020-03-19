from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate ,logout
from django.contrib import messages
from django.contrib.auth.models import User


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

def logout_user(request) :
    if request.method == "POST" :
        logout(request)
        return redirect('home')

def sign_up_user(request) :
    if request.method == "GET" :
        return render(request, 'user_auth/sign_up.html')
    elif request.method == "POST" :
        user_first_name = request.POST['first_name']
        user_last_name = request.POST['last_name']
        user_username = request.POST['username']
        user_email = request.POST['email']
        user_password1 = request.POST['password1']
        user_password2 = request.POST['password2']

    if User.objects.filter(username=user_username).exists():
        messages.info(request, 'username is taken, try another one')
        return redirect('sign_up_user')



    elif User.objects.filter(email= user_email).exists() :
        messages.info(request, 'email is taken, try another one')
        return redirect('sign_up_user')

    elif user_password1 != user_password2 :
        messages.info(request, 'password not matching')
        return redirect('sign_up_user')


    else :
        user = User.objects.create_user(first_name = user_first_name,
                                        last_name = user_last_name,
                                        username = user_username,
                                        email = user_email,
                                        password = user_password1
                                        )
        user.save();
        login(request,user)
        return redirect("home")

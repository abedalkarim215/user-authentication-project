from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate ,logout
from django.contrib import messages
from django.contrib.auth.models import User
import random


def home(request) :
    context = {
        'title' : 'Home'

    }
    return render(request,'user_auth/home.html',context)


def login_user(request):
    if request.method == "GET":
        context = {
            'title': 'Login'
        }
        return render(request, 'user_auth/login.html',context)

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
        context = {
            'title': 'Sign Up'
        }
        return render(request, 'user_auth/sign_up.html',context)
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


# generate_password function view
def generate_password(request) :
    if request.method == "GET" :
        context = {
            'title' : 'Password Generator' ,
            'range' : range(7,31) ,

        }
        return render(request,'user_auth/generate_password_function/generate_password.html', context)
    elif request.method == "POST" :
        characters = list('abcdefghijklmnopqrstuvwxyz')

        if request.POST.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.POST.get('special_characters'):
            characters.extend(list('!@#$%^&*()<>?;.'))
        if request.POST.get('numbers'):
            characters.extend(list('0123456789'))
        if request.POST.get('arabic_letters'):
            characters.extend(list('ابتثجحخدذرزسشصضطظعغفقكلمنهوي'))

        length = int(request.POST.get('length', 12))

        password_generated = ''
        for i in range(length):
            password_generated += random.choice(characters)
        context =  {
            'title' : 'the result' ,
            'password': password_generated
        }

        return render(request,
                      'user_auth/generate_password_function/generate_password_result.html',
                      context)
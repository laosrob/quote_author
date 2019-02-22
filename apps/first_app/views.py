# LOGIN VIEWS

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):

    return render(request,"first_app/index.html")

def process_users(request): # process for registering new users

    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors): # checking for errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST["email"],password=request.POST["password"],confirm_password=request.POST['confirmpw'])
        user = User.objects.get(email_address=request.POST['email'])
        request.session['user_first'] = user.first_name
        request.session['user_id'] = user.id

    return redirect("/success")

def success(request): # success page
    if 'user_first' in request.session:
        return render(request,"first_app/success.html")
    else:
        return redirect ("/")

def login(request): # login process
    if request.method == "POST":
        errors = User.objects.basic_login(request.POST)
        if len(errors): # checking for errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        else:
            user = User.objects.get(email_address=request.POST['email'])
            request.session['user_id'] = user.id
            request.session['user_first'] = user.first_name
            request.session['user_last'] = user.last_name
            print(user.first_name)

        return redirect("/quotes")

def clear(request): # logout and clear sessions
    request.session.clear()
    return redirect('/')    



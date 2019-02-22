# THE WALL VIEWS

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request): # the index page
    if 'user_first' not in request.session:
        return redirect("/")
    context = {
        "all_messages": Message.objects.all()
        
    }
    print (Message.objects.all().values())
    return render(request,"the_wallapp/index.html", context)

def message(request): # process message
    if request.method == "POST":
        errors = Message.objects.message_check(request.POST)
        if len(errors): # checking for errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/quotes")
        else:
            this_user = User.objects.get(id=request.session['user_id'])
            Message.objects.create(message=request.POST['message'], author=request.POST['name'], user = this_user)

    return redirect("/quotes")

def account(request,id): # account page

    if 'user_first' in request.session:
        context = {
        "user": User.objects.get(id=id), "user_info": User.objects.all().values(),
    }
        return render(request,"the_wallapp/account.html", context)
    else:
        return redirect ("/quotes")

def edit(request,id): # edit account process

    if request.method == "POST":
        errors = User.objects.edit_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/account/"+id+"/edit")
        else:
            account_to_update = User.objects.get(id=id)
            account_to_update.first_name = request.POST['first_name']
            account_to_update.last_name = request.POST['last_name']
            account_to_update.email_address = request.POST['email']
            account_to_update.password = request.POST['password']
            account_to_update.confirm_password = request.POST['confirmpw']
            account_to_update.save()

    return redirect("/account/"+id)    

def posted(request, id): # all post for users
    context = {
        "user": User.objects.get(id=id), "all_messages": Message.objects.all(),
    }
    return render(request,"the_wallapp/posted.html", context)

def delete_message(request, id): # delete messages
    message_to_delete = Message.objects.get(id=id)
    message_to_delete.delete()
    return redirect('/quotes')

def like_message(request, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    message.like.add(user)
    message.save()
    return redirect('/quotes')



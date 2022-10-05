from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *

def index(request):
    
    return render(request,"LoginRegistration.html")


def login(request):

    email=request.POST['email']
    password=request.POST['password']
    if user.objects.filter(email = email):
        User=user.objects.get(email = email)
        if User.password == password:
            request.session['fname']=User.fname
            request.session['reglog']=False #False indicates login while True indicates Register
            request.session['userid']=User.id
            return redirect("/success")
        else:
            messages.error(request,"password is not valid")
    else:
        messages.error(request,"email is not found")


    return redirect("/")
    # return render(request,"LoginRegistration.html")


def register(request):

    errors = user.objects.basic_validator(request.POST)
    email=request.POST['email'] 
    if user.objects.filter(email = email):
        errors['email1'] = "already existed email address!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    password=request.POST['password']  
    request.session['fname']= firstname
    request.session['reglog']= True
    thisuser=user.objects.create(fname=firstname,lname=lastname,email=email,password=password)
    request.session['userid']= thisuser.id

    return redirect("/success")


def success(request):
    if request.session['fname']:
        context = {
            "fname":request.session['fname'],
            "reglog":request.session['reglog']
        }
        return render(request,"success.html",context)
    else:
        return redirect("/success")

def logout(request):
    request.session['fname']=None
    request.session['reglog']=None
    request.session['userid']=None
    return redirect("/")

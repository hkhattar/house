
from django.shortcuts import render,redirect,reverse
from .models import User , UserManager
from django.contrib import messages
# Create your views her e.
import bcrypt

def index(request):
	return render(request,"house/index.html")

def login_reg(request):
	return render(request,"house/login.html")

def registration(request):
    if request.method=="POST":
        first=request.POST['first']
        last=request.POST['last']
        username=request.POST['username']
        email=request.POST['email']
        pin=request.POST['pin']
        confirm=request.POST['confirm']
        errors=User.objects.register_valid(first,last,email,pin,confirm,username)
        if len(errors)>0:
            print(errors)
            for error in errors:
                messages.error(request,error)
            return redirect(reverse('house:login_reg'))
        else:
            hashed=bcrypt.hashpw(pin.encode(),bcrypt.gensalt())
            user=User.objects.create(first_name=first,last_name=last,username=username,email=email,password=hashed)
            print(user.username)
            messages.success(request,"Successfully registered!")
        return render(request,'house/success.html')
 
def login(request):
    if request.method=="POST":
        login_username=request.POST['username_login']
        login_pin=request.POST['pin_login']
        if User.objects.isExist(login_username):
            if User.objects.login_valid(login_username,login_pin):
                return render(request,'house/success.html')
            else:
                messages.error(request,"login unsuccessful")
        else:
            messages.error(request,"user not exist")
        return redirect(reverse('house:login_reg'))


from django.db import models
import re
import bcrypt

email_reg=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_reg=re.compile(r'^[A-Za-z]{2,}$')
pin_reg=re.compile(r'^.{8,}$')
username_reg=re.compile(r'^[0-9a-zA-Z?-]{4,}$')

class UserManager(models.Manager):
    
    def register_valid(self,first,last,email,pin,confirm,username):
        error=[]
        if not name_reg.match(first):
            error.append("first name invalid")
        if not name_reg.match(last):
            error.append("last name invalid")
        if not email_reg.match(email):
            error.append("email invalid")
        if not pin_reg.match(pin):
            error.append("password too short")
        if pin!=confirm:
            error.append("confirm don't match with password")
        if not username_reg.match(username):
            error.append("username invalid")
        if User.objects.isExist(username):
            error.append("username is used, please choose a new one")
        return error

    def isExist(self,username):
        return User.objects.filter(username=username).exists()
    
    def login_valid(self,username,password):
        hashedpw=User.objects.get(username=username).password.encode()
        if bcrypt.hashpw(password.encode(),hashedpw)==hashedpw:
            return True
        else:
            return False

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


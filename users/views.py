
from django.shortcuts import render,redirect
from django.contrib import messages
from .register import Usersregistration
from django.contrib.auth.models import User

def register(request):
    if request.method=='POST':
       register=Usersregistration(request.POST)
       if register.is_valid():
           register.save()
           username=register.cleaned_data.get('username')
           messages.success(request,f'Account Created ')
           return redirect('Login')
    else:
       register=Usersregistration()
    return render(request,'users/register.html',{'register':register})


def home(request):
    return render(request,'users/home.html')
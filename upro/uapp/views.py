from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def main(request):
    return render(request,'welcome.html')

def login_user(request):
    login(request):
        


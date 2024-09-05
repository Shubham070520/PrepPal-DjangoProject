from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from App.models import Candidate,Questions,Result
from django.contrib.auth.models import User
from django.contrib import messages #to add message
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q  #to write min and max values
import random
from django.core.mail import send_mail


def welcome(request):
    return render(request,'home.html')

def candidateRegForm(request):
    return render (request,'signup.html')

def candidateRegistration(request):
    if request.method == "POST":
        u = request.POST['username']
        # to check if the username already exists 
        if Candidate.objects.filter(username=u).exists():
            messages.error(request,'Username already exists')
        else:
            pass


def loginView(request):
    return render(request,'login.html')

def otp(request):
    return render(request,'login1.html')

def candidateHome(request):
    pass

def testPaper(request):
    pass

def calcTestRes(request):
    pass

def testResHistory(request):
    pass

def showTestRes(request):
    pass

def logoutView(request):
    pass








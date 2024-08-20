from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from App.models import Candidate,Questions,Result
from django.contrib.auth.models import User
from django.contrib import messages #to add message
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q  #to write min and max values


def welcome(request):
    pass

def candidateRegForm(request):
    pass

def candidateRegistration(request):
    pass

def loginView(request):
    pass

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








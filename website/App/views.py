from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from App.models import Candidate,Questions,Result
from django.contrib.auth.models import User
from django.contrib import messages #to add message
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q  #to write min and max  values
import random
import re
from django.contrib.auth.hashers import make_password #Used Django's built-in make_password function to hash the password before storing it in the database.
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
            return render(request, 'signup.html')
        else:
            # to capture values
            e = request.POST['email']
            n = request.POST['number']
            p = request.POST['password']
            cp = request.POST['confirm_password']
            # validation
            if u=='' or e=='' or p=='' or cp== '' or n =='':
                messages.error(request,'All fields are compulsory')
                return render(request,'signup.html')
            
            if p != cp:
                messages.error(request,"Passwords don't match")
                return render(request,'signup.html')
            
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', e):  #The re.match() function is used to match the regex pattern against the input email address e.
                
                 #Regex Pattern elaboration
                # ^ matches the start of the string
                # [a-zA-Z0-9_.+-]+ matches one or more of the following characters:
                # a-z (lowercase letters)
                # A-Z (uppercase letters)
                # 0-9 (digits)
                # _ (underscore)
                # . (dot)
                # + (plus sign)
                # - (hyphen)
                # @ matches the @ symbol
                # [a-zA-Z0-9-]+ matches one or more of the following characters:
                # a-z (lowercase letters)
                # A-Z (uppercase letters)
                # 0-9 (digits)
                # - (hyphen)
                # \. matches a period (.) character
                # [a-zA-Z0-9-.]+ matches one or more of the following characters:
                # a-z (lowercase letters)
                # A-Z (uppercase letters)
                # 0-9 (digits)
                # - (hyphen)
                # . (dot)
                # $ matches the end of the string

                messages.error(request, 'Invalid email address')
                return render(request, 'signup.html')
            
            if len(p)<8:
                messages.error(request, 'Password must be at least 8 characters long')
                return render(request, 'signup.html')
            
            
            #Create a New Candidate
            # else:
            try:    #Added a try-except block to catch any unexpected errors during registration.
                o = Candidate.objects.create(username= u,email=e,password=p,phone = n)
                o.save()
                messages.success(request,'Registered successfully,Please Login')
                return redirect('/login')
            except Exception as e:
                messages.error(request, 'An error occurred during registration')
                return render(request, 'signup.html')
    else:
        return render(request,'signup.html')


def loginView(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
    #     user = authenticate(username=u, password=p)
    #     if user == None: #for verifying user
    #         messages.error(request, 'Invalid credentials')
    #         return render(request, 'login.html')
    #     else:
    #         login(request, user)
    #         messages.success(request,'Logged in successfully!')
    #         return redirect('home-content.html')
    # else:
    #     return render(request, 'login.html')
    
    #     try:
    #         user = Candidate.objects.get(username=u)
    #         if user.check_password(p): # Verify the password
    #             login(request, user)
    #             messages.success(request,'Logged in successfully!')
    #             return redirect('home-content.html')
    #         else:
    #             messages.error(request, 'Invalid credentials')
    #             return render(request, 'login.html')
    #     except Candidate.DoesNotExist:
    #         messages.error(request, 'Invalid credentials')
    #         return render(request, 'login.html')
    # else:
    #     return render(request, 'login.html')
        try:
            user = Candidate.objects.get(username=u)
            if user.check_password(p): # Verify the password
                # Create a session for the user
                request.session['username'] = u
                login(request, user)
                messages.success(request,'Logged in successfully!')
                return redirect('home-content.html')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect(request, 'login.html')
        except Candidate.DoesNotExist:
            messages.error(request, 'Invalid credentials')
            return redirect(request, 'login.html')
    else:
        return render(request, 'login.html')

def otp(request):
    return render(request,'login1.html')

def candidateHome(request):
    return render(request,'home-content.html')

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



# def loginView(request):
#     if request.method == 'POST':
#         u = request.POST['username']
#         p = request.POST['password']
#         try:
#             user = Candidate.objects.get(username=u)
#             if user.check_password(p): # Verify the password
#                 # Create a session for the user
#                 request.session['username'] = u
#                 request.session['user_id'] = user.id
#                 login(request, user)
#                 messages.success(request,'Logged in successfully!')
#                 return redirect('home-content.html')
#             else:
#                 messages.error(request, 'Invalid credentials')
#                 return render(request, 'login.html')
#         except Candidate.DoesNotExist:
#             messages.error(request, 'Invalid credentials')
#             return render(request, 'login.html')
#     else:
#         return render(request, 'login.html')

# def logoutView(request):
#     try:
#         # Clear the session
#         del request.session['username']
#         del request.session['user_id']
#     except KeyError:
#         pass
#     logout(request)
#     messages.success(request, 'Logged out successfully!')
#     return redirect('login.html')

# def candidateHome(request):
#     if 'username' in request.session:
#         # Get the user's details from the session
#         username = request.session['username']
#         user_id = request.session['user_id']
#         user = Candidate.objects.get(id=user_id)
#         return render(request, 'home-content.html', {'user': user})
#     else:
#         return redirect('login.html')

# def testPaper(request):
#     if 'username' in request.session:
#         # Get the user's details from the session
#         username = request.session['username']
#         user_id = request.session['user_id']
#         user = Candidate.objects.get(id=user_id)
#         return render(request, 'test-paper.html', {'user': user})
#     else:
#         return redirect('login.html')

# def calcTestRes(request):
#     if 'username' in request.session:
#         # Get the user's details from the session
#         username = request.session['username']
#         user_id = request.session['user_id']
#         user = Candidate.objects.get(id=user_id)
#         return render(request, 'calc-test-res.html', {'user': user})
#     else:
#         return redirect('login.html')

# def testResHistory(request):
#     if 'username' in request.session:
#         # Get the user's details from the session
#         username = request.session['username']
#         user_id = request.session['user_id']
#         user = Candidate.objects.get(id=user_id)
#         return render(request, 'test-res-history.html', {'user': user})
#     else:
#         return redirect('login.html')

# def showTestRes(request):
#     if 'username' in request.session:
#         # Get the user's details from the session
#         username = request.session['username']
#         user_id = request.session['user_id']
#         user = Candidate.objects.get(id=user_id)
#         return render(request, 'show-test-res.html', {'user': user})
#     else:
#         return redirect('login.html')




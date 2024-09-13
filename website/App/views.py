from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from App.models import Candidate,Questions,Result
from django.contrib.auth.models import User
from django.contrib import messages #to add message
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q  #to write min and max  values
import random
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password #Used Django's built-in make_password function to hash the password before storing it in the database.
from django.core.mail import send_mail
from django.core.paginator import Paginator  #Django’s Paginator class can be used to handle large numbers of questions more efficiently.


def welcome(request):
    registered_students_count = Candidate.objects.count()

    return render(request,'home.html',{
        'registered_students_count': registered_students_count,
    })

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


# def loginView(request):
#     print("entering loginView function")
#     if request.method == 'POST':
#         u = request.POST.get('username') 
#         p = request.POST.get('password')
#         # The get method is used to retrieve the value for the specified key ('key') from the QueryDict. If the key is not found, it returns the specified default value (default) instead of raising an error.
#         print(f"username: {u}, password: {p}")
#         if not u or not p:
#             messages.error(request, 'Please fill in both username and password.')
#             return redirect('App:login')
#         # else:
#         user = authenticate(username=u, password=p)
#         user = User.objects.get(username=u)
#         print(user.is_active)

#         print('this is name of user',user)
#         try:
#             print(f"Authenticated User: {user}")  #why it is showing none
#             if user is not None:
#                 login(request, user)  # This will set the session automatically
#                 request.session['name'] = user.username
#                 print(f"User {user.username} logged in successfully.")
#                 messages.success(request, 'Logged in successfully!')
#                 return render(request,'App:home')
#             else:
#                 messages.error(request, 'Invalid credentials')
#                 return redirect('App:login')
#         except Exception as e:
#             print(f"Error during authentication: {e}")
#             messages.error(request, 'An error occurred during authentication')
#             return redirect('App:login')
#     else: 
#           return render(request, 'login.html')

# def loginView(request):
#     if request.method == 'POST':
#         u = request.POST.get('username') 
#         p = request.POST.get('password')
        
#         if not u or not p:
#             messages.error(request, 'Please fill in both username and password.')
#             return redirect('App:login')
        
#         # Check if user exists before authentication
#         try:
#             user = User.objects.get(username=u)
#         except ObjectDoesNotExist:
#             messages.error(request, 'No user with this username exists')
#             return redirect('App:login')
        
#         # Authenticate user
#         user = authenticate(username=u, password=p)
#         if user is not None:
#             login(request, user)
#             request.session['name'] = user.username
#             messages.success(request, 'Logged in successfully!')
#             return render(request, 'App:home')
#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('App:login')
#     else:
#         return render(request, 'login.html')

def loginView(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        c = Candidate.objects.filter(username=u, password=p)
        if len(c) == 0:
            messages.error(request, 'Invalid credentials')
            return redirect('App:login')
        else:
            request.session['username'] = c[0].username
            request.session['name'] = c[0].name
            return redirect('App:home')
    
# def welcome1(request):
#     if 'username' not in request.session.keys():
#         return redirect('login')

def otp(request):
            return render(request,'login1.html')

# @login_required(login_url='login')  #checks if the user is authenticated and redirects them to the login page if they are not. The login_url='login' argument ensures that it uses the correct login URL.
# def candidateHome(request):
#     #if request.user.is_authenticated:
#     user = request.user
#     return render(request, 'home-content.html')
#     # else:
#     #     return redirect('login')

def candidateHome(request):
    if 'username' not in request.session.keys():
        return redirect('login')
    else:
        return render(request, 'home-content.html')

def testPaper(request):
    if 'username' not in request.session.keys():
        return redirect('login/')
    # n = int(request.GET['n'])
    # question_pool = list(Questions.objects.all())
    # random.shuffle(question_pool)
    # question_list = question_pool[:n]
    # context = {'questions' : question_list}
    # return render(request, 'test-paper.html',context)
    n = int(request.GET.get('n', 10))  # Number of questions to fetch (default to 10)
    que_pool = list(Questions.objects.all())  # Retrieve all questions
    random.shuffle(que_pool)  # Shuffle the question list randomly
    que_list = que_pool[:n]  # Select 'n' questions

    # Pass the list of questions to the template
    context = {'Questions': que_list}
    return render(request, 'test-paper.html', context)

def calcTestRes(request):
    if 'username' not in request.session.keys():
        return redirect('login')
    total_attempt = 0
    total_right = 0
    total_wrong = 0
    test_score = 0
    qid_list = []
    for i in request.POST:
        if i.startswith('q_no'):  #data send through hidden input
            qid_list.append(int(request.POST[i]))  #aim is to know the id of the submitted questions
    for n in qid_list:
        question = Questions.objects.get(que_id = n)  #want to fetch those questions which came in the question paper from database
        try:
            if question.correct_ans == request.POST['q'+str(n)]:
                total_right += 1
            else:
                total_wrong += 1
            total_attempt += 1
        # except:
        #     pass
        except Exception as e:
                # Log any other unexpected errors for debugging
                print(f"Error processing question {n}: {e}")
    test_score = (total_right-total_wrong)/len(qid_list)*10
    #to store result in result table
    result = Result()  #made object
    result.username = Candidate.objects.get(username = request.session['username'])  #since foreign key,we have to assign object from candidate table
    result.attempts = total_attempt
    result.right_attempts = total_right
    result.wrong_attempts = total_wrong
    result.test_score = test_score
    result.save()
    #to make changes in candidate table
    candidate = Candidate.objects.get(username = request.session['username'])   #to make changes in logged in candidate
    candidate.test_attempted += 1  #after giving test +1 attempt
    candidate.test_score = (candidate.test_score*(candidate.test_attempted-1)+test_score)/candidate.test_attempted
    candidate.save()
    return redirect('result/')


def testResHistory(request):
    #to fetch every rows with username which is logged in
    if 'username' not in request.session.keys():
        return redirect('login')
    candidate = Candidate.objects.filter(username = request.session['username'])
    results = Result.objects.filter(username_id = candidate[0].username)
    #filter function always returns query set i.e collection of objects but we it will be giving 1 object cause it is 1 for now.
    #get function gives 1 object
    context = {'results':results, 'candidate':candidate}
    return render(request,'candidate_history.html',context)


def showTestRes(request):
    if 'username' not in request.session.keys():
        return redirect('login')
    #fetch latest result from result table
    # result = Result.objects.filter(username = Candidate.objects.get(username = request.session['username'])).latest('res_id')
    result = Result.objects.filter(res_id = Result.objects.latest('res_id').res_id,username_id = request.session['username'])  #2 things are passed in filter = result_id and username of loggedin user
    context = {'result':result}
    return render(request, 'show_result.html',context)

def logoutView(request):
    # logout(request)  #user object is in request
    # messages.success(request,'Logged out successfully!')
    # return redirect('/')
    if 'username' in request.session.keys():
        del request.session['username']
        del request.session['name']
    return redirect('/login')


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




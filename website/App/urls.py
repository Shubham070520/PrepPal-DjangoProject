from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views
app_name= 'App'

urlpatterns = [
    path('',views.welcome),  #http://127.0.0.1:8000/
    path('candidateRegistration',views.candidateRegForm),   #signup.html ,name="registrationForm"
    path('store-candidate',views.candidateRegistration), #name='store-candidate'
    path('login',views.loginView), #name="login"
    path('otp',views.otp),
    path('home',views.candidateHome), #redirect after login
    path('testPaper',views.testPaper),
    path('calc-Result',views.calcTestRes),
    path('test-History',views.testResHistory),
    path('result',views.showTestRes),
    path('logout',views.logoutView),

]
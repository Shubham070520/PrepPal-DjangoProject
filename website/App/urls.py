from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = [
    path('',views.welcome),
    path('candidateRegistration',views.candidateRegForm),
    path('submit',views.candidateRegistration),
    path('login',views.loginView),
    path('otp',views.otp),
    path('home',views.candidateHome),
    path('testPaper',views.testPaper),
    path('calc-Result',views.calcTestRes),
    path('test-History',views.testResHistory),
    path('result',views.showTestRes),
    path('logout',views.logoutView),

]
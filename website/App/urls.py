from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views
app_name= 'App'   # Define app name for namespacing

urlpatterns = [
    path('',views.welcome,name="welcome"),  #http://127.0.0.1:8000/
    path('homelog/',views.homelog,name="homelog"), #after login
    path('candidateRegistration',views.candidateRegForm,name="candidateRegistration"),   #signup.html ,name="registrationForm"
    path('store-candidate',views.candidateRegistration,name="store-candidate"), #name='store-candidate'
    path('login/' ,views.loginView, name="login"), 
    path('otp',views.otp,name="otp-verification"),
    path('home',views.candidateHome,name="home"), #redirect after login
    path('test-Paper',views.testPaper,name="test-paper"),
    path('calc-Result',views.calcTestRes,name="calc-Result"),
    path('test-history',views.testResHistory,name="test-history"),
    path('result/',views.showTestRes,name="showresult"),
    path('logout',views.logoutView,name="logout"),
    path('pass',views.buypass , name="pass"),
    path('test',views.testSeries, name ="test"),
    path('notes',views.notes,name="notes"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
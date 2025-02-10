# Project Report: PrepPal

## 1. Introduction
PrepPal is an online examination system designed to facilitate seamless test-taking experiences for candidates. It enables users to register, take tests, view their results, purchase study plans, and access study materials. The system is built using Django and integrates functionalities such as user authentication, test paper generation, result calculation, and online payments.

## 2. Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite / PostgreSQL
- **Payment Integration:** Razorpay
- **Security:** Django Authentication System

## 3. Key Features

- **User Authentication:** Registration, Login, Logout with session handling.
- **Test Management:** Randomized test paper generation from a question bank.
- **Result Calculation:** Tracks attempts, right/wrong answers, and scores.
- **Exam Records:** Stores user test history and performance analysis.
- **Study Plans:** Subscription-based access to study materials.
- **Notes Section:** Provides downloadable PDFs for study material.
- **Admin Panel:** Allows management of users, tests, results, and plans.
- **Payment Gateway:** Razorpay integration for purchasing plans.

## 4. Database Schema Overview
The database schema consists of multiple models in Django, as shown below:

### Candidate Model: Stores user information.
```python
class Candidate(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False)
    test_attempted = models.IntegerField(default=0)
    test_score = models.FloatField(default=0)
    email = models.EmailField(max_length=30, null=False)
    phone = models.BigIntegerField(null=False)
```

### Exam Model: Defines different types of exams.
```python
class Exam(models.Model):
    name = models.CharField(max_length=255)
    exam_type = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
```

### Questions Model: Stores questions with multiple-choice options.
```python
class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=False)
    que_id = models.BigAutoField(primary_key=True)
    que = models.TextField()
    opt_1 = models.CharField(max_length=255)
    opt_2 = models.CharField(max_length=255)
    opt_3 = models.CharField(max_length=255)
    opt_4 = models.CharField(max_length=255)
    correct_ans = models.CharField(max_length=255)
    def __str__(self):
        return self.que
```

### Result Model: Tracks test attempts and scores.
```python
class Result(models.Model):
    res_id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date_attempted = models.DateTimeField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempts = models.IntegerField()
    right_attempts = models.IntegerField()
    wrong_attempts = models.IntegerField()
    test_score = models.FloatField()
```

### Plans Model: Defines study subscription plans.
```python
class Plans(models.Model):
    price = models.IntegerField()
    plan_type = models.CharField(max_length=255, default='Monthly Pass')
    validity = models.CharField(max_length=255, default='Valid for 30 Days')
    def __str__(self):
        return self.plan_type
```

### Notes Model: Stores downloadable study materials.
```python
class Notes(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')
    def __str__(self):
        return self.title
```

## 5. Project Workflow

### a) User Registration/Login → Candidates sign up and log in.
```python
path('candidateRegistration', views.candidateRegForm, name='candidateRegistration'),
path('store-candidate', views.candidateRegistration, name='store-candidate'),
path('login/', views.loginView, name='login'),
```

### b) Exam Selection → Users choose an available test.
```python
path('test-Paper', views.testPaper, name='test-paper'),
```

### c) Test Submission → Candidate submits answers.
```python
path('calc-Result', views.calcTestRes, name='calc-Result'),
```

### d) Result Calculation → System evaluates performance and updates records.
```python
path('result/', views.showTestRes, name='showresult'),
```

### e) Test History Viewing → Users can view their previous test results.
```python
path('test-history', views.testResHistory, name='test-history'),
```

### f) Plan Subscription → Users can purchase study plans via Razorpay.
```python
path('pass', views.buypass, name='pass'),
```

### g) Access Study Materials → Subscribed users can download PDFs.
```python
path('notes', views.notes, name='notes'),
```

## 6. Admin Panel Functionalities
Django's admin panel allows the management of users, exams, questions, results, and plans.
```python
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'name', 'test_attempted', 'test_score', 'email', 'phone']
    list_filter = ['username', 'email']
    search_fields = ['username', 'email']
admin.site.register(Candidate, CandidateAdmin)
```
Similarly, other models like `Questions`, `Result`, `Plans`, and `Notes` are registered in the admin panel.


from django.db import models
from django.contrib.auth.models import User
import random

class Candidate(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30,null=False)
    name = models.CharField(max_length=30,null=False)
    test_attempted = models.IntegerField(default=0)
    test_score = models.FloatField(default=0)     #+1    -0.33
    email = models.EmailField(max_length=30,null=False)   #email validator
    phone = models.BigIntegerField(null= False)


class Exam(models.Model):
    name = models.CharField(max_length=255)
    exam_type = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=False,default=1)  #One exam can have many questions
    que_id = models.BigAutoField(primary_key=True,auto_created=True)
    que = models.TextField()
    opt_1 = models.CharField(max_length=255)
    opt_2 = models.CharField(max_length=255)
    opt_3 = models.CharField(max_length=255)
    opt_4 = models.CharField(max_length=255)
    correct_ans = models.CharField(max_length=255)

    def __str__(self):
        return self.que

class Result(models.Model):
    res_id = models.BigAutoField(primary_key=True,auto_created=True)
    username = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    date_attempted = models.DateTimeField(auto_now=True)  #date to be filled automatically
    time = models.TimeField(auto_now=True) #time to be filled automatically
    attempts = models.IntegerField()
    right_attempts = models.IntegerField()
    wrong_attempts = models.IntegerField()
    test_score = models.FloatField()

# class OTP(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     otp = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def generate_otp(self):
#         return str(random.randint(100000, 999999))

class Plans(models.Model):
    price = models.IntegerField()
    plan_type = models.CharField(max_length=255,default='Monthly Pass')
    validity = models.CharField(max_length=255,default= 'Valid for 30 Days')

    def __str__(self):
        return self.plan_type


class Notes(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title


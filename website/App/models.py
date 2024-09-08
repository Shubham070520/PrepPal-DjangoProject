from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30,null=False)
    name = models.CharField(max_length=30,null=False)
    test_attempted = models.IntegerField(default=0)
    test_score = models.FloatField(default=0)     #+1    -0.33
    email = models.EmailField(max_length=30,null=False)   #email validator
    phone = models.BigIntegerField(null= False)

class Questions(models.Model):
    que_id = models.BigAutoField(primary_key=True,auto_created=True)
    que = models.TextField()
    opt_1 = models.CharField(max_length=255)
    opt_2 = models.CharField(max_length=255)
    opt_3 = models.CharField(max_length=255)
    opt_4 = models.CharField(max_length=255)
    correct_ans = models.CharField(max_length=255)

class Result(models.Model):
    res_id = models.BigAutoField(primary_key=True,auto_created=True)
    username = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    date_attempted = models.DateTimeField(auto_now=True)  #date to be filled automatically
    time = models.TimeField(auto_now=True) #time to be filled automatically
    attempts = models.IntegerField()
    right_attempts = models.IntegerField()
    wrong_attempts = models.IntegerField()
    test_score = models.FloatField()



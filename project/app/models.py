from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    slno = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    phone = models.IntegerField(unique=True)
    dept = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    hire_date = models.DateField()
    profile_pic = models.ImageField()
    

class Register(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    

from django import forms
from app.models import *


class EmployeeFrom(forms.ModelForm):
    class Meta:
        model=Employee
        exclude = ['slno']
        

        
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        help_texts = {'username':''}
        
        
class FilterFrom(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['slno','age','salary','phone','hire_date','profile_pic']
        
from django.shortcuts import render, HttpResponse
from app.models import *
from app.forms import *
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from random import randint
from django.core.mail import send_mail

# Create your views here.

def home(request):
    if request.session.get('username'):
        un = request.session.get('username')
        d = {'un':un}
        return render(request, 'home.html', d)
    return render(request,'home.html')

@login_required
def all_emp(request):
    emps = Employee.objects.all()
    d={'emps':emps}
    return render(request,'all_emp.html',d)

@login_required
def add_emp(request):
    emps = EmployeeFrom()
    d={'emps':emps}
    if request.method == 'POST' and request.FILES:
        emps = EmployeeFrom(request.POST,request.FILES)
        if emps.is_valid():
            emps.save()
            return HttpResponse('successfull')
        return HttpResponse('invalit_data(Your data is alredy exits)')
    return render(request,'add_emp.html',d)

@login_required
def remove_emp(request):
    emps = Employee.objects.all()
    d={'emps':emps}
    if request.method == 'GET':
        slno = request.GET.get('slno')
        Employee.objects.filter(slno=slno).delete()
        emps = Employee.objects.all()
        d={'emps':emps}
    return render(request,'remove_emp.html',d)
    
    
def filter_emp(request):
    return render(request,'filter_emp.html')
            
slno=0
@login_required
def update_emp(request):
    empf = EmployeeFrom()
    d={'empf':empf}
    if request.method == 'GET':
        global slno
        slno = request.GET.get('slno')
        return render(request,'update_emp.html', d)
            
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        phone = request.POST.get('phone')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        hire_date = request.POST.get('hire_date')
        profile_pic = request.POST.get('profile_pic')
        Employee.objects.filter(slno=slno).update(first_name=first_name,last_name=last_name,age=int(age),salary=salary, phone=phone, dept=dept, role=role, hire_date=hire_date, profile_pic=profile_pic)
        
        emp = Employee.objects.all()
        d={'emp':emp}
        return render(request,'remove_emp.html',d)
    return render(request, 'update_emp.html',d)
        
       
   
def register(request):
    UFO=RegisterForm()
    d={"UFO":UFO}
    if  request.method == 'POST':
        UFDO = RegisterForm(request.POST)
        if UFDO.is_valid():
            MUFDO = UFDO.save(commit=False)
            pw = UFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            return render(request,'login.html')
        return HttpResponse('invalidedata')
    return render(request,"register.html",d) 
    
def user_login(request):
    if request.method=='POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw) 
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('invlit data')
    return render(request, 'login.html')
        
@login_required         
def user_Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def forget_password(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        UO = User.objects.get(username=un)
        if UO:
            email = UO.email
            otp = randint(10000,999999)
            send_mail(
                'OTP',
                f"OTP is {otp}",
                'likith.qsp@gmail.com',
                [email],
                fail_silently=False
            )
            request.session['username'] = un
            request.session['otp'] = otp
            
            return render(request,'verification.html')
        return HttpResponse('invalit')
    return render(request, 'forget_password.html')

def verification(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        cotp = request.session.get('otp')
        if cotp == int(otp):
            return render(request, 'password.html')
        else:
            return HttpResponse(f'invalid OTP {otp} {cotp}')
    else:
        return render(request, 'varification.html')
    
    
def password(request):
    if request.method == 'POST':
        pw = request.POST.get('pw')
        un = request.session.get('username')
        print(un)
        UO = User.objects.get(username=un)
        if UO:
            UO.set_password(pw)
            UO.save()
            return render(request,'login.html')
    else:
        return render(request, 'password.html')
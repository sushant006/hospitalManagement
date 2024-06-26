from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor,Patient
# Create your views here.
def About(request):
    return render(request,'about.html');

def Home(request):
    return render(request,'home.html');

def Contact(request):
    return render(request, 'contact.html');

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request,user)
                error = "No"

            else:
                error = "Yes"
        except:
            error = "Yes"
    d = {'error' : error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')
def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id = pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['Name']
        m = request.POST['mobile']
        sp = request.POST['special']
       
        try:
            Doctor.objects.create(Name = n, mobile = m, special = sp)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc':doc}
    return render(request,'view_patient.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id = pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['Name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
       
        try:
            Patient.objects.create(Name = n,gender = g, mobile = m, address = a)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}
    return render(request,'add_patient.html',d)




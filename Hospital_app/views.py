from django.shortcuts import render, redirect
from .models import Doctor, Patient
from .forms import doctor_form, patient_form, Userform
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(req):
    return render(req, 'base.html')

def patient_1(req):
    d = Patient.objects.all().values()
    return render(req, 'Patient.html', {'patient':d})

def add_appointment(req):
    if req.method == 'POST':
        d = patient_form(req.POST)
        if d.is_valid():
            d.save()
            return redirect('appointment')
        else:
            return HttpResponse('Your form input is wrong')
            return redirect('appointment')
    else:
        d = patient_form()
    return render(req, 'add_appointment.html', {'add':d})

def doctor(req):
    d = Doctor.objects.all().values()
    return render(req, 'doctor.html',{'data':d})

def add_doctor(req):
    if req.method == 'POST':
        d = doctor_form(req.POST)
        if d.is_valid():
            d.save()
            return redirect('to_doctor')
        else:
            return HttpResponse('Your form input is wrong')
            return redirect('to_doctor')
    else:
        d = doctor_form()
    return render(req, 'add_doctor.html', {'add':d})

def edit_appointment(req, p_id):
    p_id = int(p_id)
    try:
        p_sel = Patient.objects.get(id=p_id)
    except Patient.DoesNotExist:
        return redirect('appointment')
    else:
        d = patient_form(req.POST or None, instance=p_sel)
        if d.is_valid():
            d.save()
            return redirect('appointment')
    return render(req, 'add_appointment.html', {'add':d})

def del_appointment(req, p_id):
    p_id = int(p_id)
    try:
        p_sel = Patient.objects.get(id = p_id)
    except Patient.DoesNotExist:
        return redirect('appointment')
    else:
        d = p_sel.delete()
        return redirect('appointment')

def update_doctor(req, d_id):
    try:
        d_sel = Doctor.objects.get(doctor_name=d_id)
    except Doctor.DoesNotExist:
        return redirect('to_doctor')
    else:
        d = doctor_form(req.POST or None, instance=d_sel)
        if d.is_valid():
            d.save()
            return redirect('to_doctor')
    return render(req, 'add_doctor.html', {'add':d})

def del_doc(req, d_id):
    try:
        d_sel = Doctor.objects.get(doctor_name = d_id)
    except Doctor.DoesNotExist:
        return redirect('to_doctor')
    else:
        d = d_sel.delete()
        return redirect('to_doctor')

def register(req):
    if req.method == 'POST':
        abc = Userform(req.POST)
        if abc.is_valid():
            user = abc.save()
            login(req, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid Input')
    else:
        abc = Userform()
    return render(req, 'register.html', {'register':abc})

def logout_request(req):
    logout(req)
    return redirect('login')

def login_request(req):
    if req.method == 'POST':
        abc = AuthenticationForm(req, data=req.POST)
        if abc.is_valid():
            username = abc.cleaned_data.get('username')
            password = abc.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('home')
            else:
                return HttpResponse('Invalid credentials')
        else:
            return HttpResponse('Invalid Credentials')
    abc = AuthenticationForm()
    return render(req, 'login.html', {'login':abc})

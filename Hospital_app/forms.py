from django import forms
from .models import Doctor, Patient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class doctor_form(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class Userform(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')
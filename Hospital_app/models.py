from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100, primary_key=True)
    Degree = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100, blank=True)

class Patient(models.Model):
    Patient_name = models.CharField(max_length=100)
    appointment_with = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
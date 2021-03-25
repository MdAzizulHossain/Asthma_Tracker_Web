from django.db import models

# import in-Built User Models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12, default="", unique=True)
    email = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    age = models.IntegerField(max_length=12)
    weight = models.IntegerField(max_length=3)
    blood = models.CharField(max_length=10)
    medical = models.CharField(max_length=100)
    case = models.CharField(max_length=20)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    spo2 = models.DecimalField(max_digits=5, decimal_places=2)
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)


class Invoice(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    outstanding = models.CharField(max_length=10)
    paid = models.CharField(max_length=10)

class report(models.Model):
    spo2 = models.DecimalField(max_digits=5, decimal_places=2)
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)


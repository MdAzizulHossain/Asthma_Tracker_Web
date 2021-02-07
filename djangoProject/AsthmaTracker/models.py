from django.db import models
# from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField( max_length=50, unique=True)
    phone = models.CharField(max_length=12, default="", unique=True)
    regno = models.CharField(max_length=50, unique=True)
    spcl = models.CharField(max_length=20)
    gender = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    blood = models.CharField(max_length=10)


    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Doctor List"
        verbose_name_plural = "Doctor Database"


class Patient(models.Model):
    name = models.CharField(max_length=50)
    psw = models.CharField(max_length=8)
    mobile = models.IntegerField(null=True)
    email = models.CharField(null=True, max_length=50)
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(null=True, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

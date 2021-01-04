from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(max_length=13)
    email = models.CharField(null=True, max_length=50)
    special = models.CharField(max_length=50)
    password = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    email = models.CharField(null=True, max_length=50)
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(null=True, max_digits=3, decimal_places=2)




    def __str__(self):
        return self.name



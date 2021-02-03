from django.db import models


# from django.contrib.auth.models import (
#     AbstractBaseUser, BaseUserManager
#                                         )

# Create your models here.
# class User(AbstractBaseUser):
#
#     email           =   models.EmailField(max_length=255, unique=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)  # a admin user; non super-user
#     admin = models.BooleanField(default=False)  # a superuser
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email
#
#     def __str__(self):  # __unicode__ on Python 2
#         return self.email
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff
#
#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin
#
#     @property
#     def is_active(self):
#         "Is the user active?"
#         return self.active


class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)
    # bmdc_reg = models.CharField(max_length=10)
    specialization = models.CharField(max_length=255)
    password = models.CharField(null=True, max_length=50)

    def __str__(self):
        return str(self.email)

    # class Meta:
    #     verbose_name = "Doctor List"
    #     verbose_name_plural = "Doctor Database"


class Patient(models.Model):
    name = models.CharField(max_length=50)
    psw = models.CharField(max_length=8)
    mobile = models.IntegerField(null=True)
    email = models.CharField(null=True, max_length=50)
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(null=True, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(verbose_name='Email address', unique=True)
    designation = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10,null=True)
    date_of_registration = models.DateTimeField(auto_now_add=True)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from .models import models



# class User(AbstractUser):
#     is_admin = models.BooleanField(default=False)
#     is_cashier = models.BooleanField(default=False)

#     class Meta:
#         swappable = 'AUTH_USER_MODEL'

class User(models.Model):
    username = models.CharField(max_length=100)
    # Add more fields as per your requirements

    def _str_(self):
        return self.username

    def _str_(self):
        return self.email




class RegisteredCar(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20)
    vehicle_color = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    register_name = models.CharField(max_length=200)
    comment = models.TextField()




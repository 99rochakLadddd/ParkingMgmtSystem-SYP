from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


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


# class Customer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=100)
#     car_model = models.CharField(max_length=100)
#     car_color = models.CharField(max_length=100)
#     comment = models.TextField(max_length=5000, blank=True)
#     cost_per_day = models.IntegerField(null=True, blank=True)
#     register_name = models.CharField(max_length=100)
#     reg_date = models.DateTimeField(auto_now_add=True)
#     exit_date = models.DateTimeField(null=True, blank=True)    
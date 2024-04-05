from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

from django.db import models

class NewCarRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20)
    vehicle_color = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    register_name = models.CharField(max_length=100)  # This matches the input field name
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.vehicle_number}"
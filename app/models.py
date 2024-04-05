from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

    def _str_(self):
        return self.email



class NewCarRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20)
    vehicle_color = models.CharField(max_length=30)
    model_number = models.CharField(max_length=50)
    register_name = models.CharField(max_length=100)
    comment = models.TextField()
    
    def __str__(self):
        return self.vehicle_number



from django import forms
from .models import RegisteredCar

class RegisterCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['car_model'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['car_color'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cost_per_day'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['phone_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['comment'].widget.attrs = {
            'class': 'form-control col-md-6'
        } 
        self.fields['is_payed'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
    class Meta:
        model = RegisteredCar
        fields = ("first_name","last_name","vehicle_number","vehicle_color","phone_number","comment","register_name")

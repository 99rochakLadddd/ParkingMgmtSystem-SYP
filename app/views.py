from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout  # Import the logout function
from .models import RegisteredCar
from django.contrib import messages


def home(request):
    return render(request, "index.html")

def login_view(request):
    if request.method=='POST':
        userEmail = request.POST.get("email")
        password = request.POST.get("password")
        print(f"email entered is {userEmail}  and the password is {password}")
    return render(request, 'login.html')

def register_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"the user details for registration are {email} {username} and password is {password}")
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def index_view(request):
    return render(request, 'index.html')

def new_car_registration_view(request):
    # Your view logic goes here
    return render(request, 'new_car_registration.html')

def manage_user_view(request):
    return render(request, 'manage_user.html')

# Other view functions remain unchanged
def admin_view(request):
    # Your admin view logic goes here
    return render(request, 'admin_view.html')

######updated from gpt#####
def new_car_registration(request):
    if request.method == 'POST':
        ##retrieving user input
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        vehicle_number = request.POST.get('vehicle_number')
        vehicle_color = request.POST.get('vehicle_color')
        model_number = request.POST.get('model_number')
        register_name = request.POST.get('register_name')
        comment = request.POST.get('comment')

        # Save the submitted data to the database
        r = RegisteredCar(first_name = first_name, last_name = last_name, phone_number = phone_number, vehicle_number = vehicle_number, vehicle_color = vehicle_color, model_number = model_number, register_name = register_name, comment = comment)
        r.save()
        messages.success(request, 'Vehicle Registered Successfully')

    return redirect('new_car_registration')
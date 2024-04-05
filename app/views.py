from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 
from .models import NewCarRegistration
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import User

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

def thankyou_view(request):
    return render(request, 'thankyou_carreg.html')

def manage_user_view(request):
    return render(request, 'manage_user.html')


# Other view functions remain unchanged
def admin_view(request):
    # Your admin view logic goes here
    return render(request, 'admin_view.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'manage_user.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        # Form validation
        if not (name and email and address and phone):
            messages.error(request, 'All fields are required.')
            return redirect('user_list')
        
        # Create new user
        try:
            User.objects.create(
                name=name,
                email=email,
                address=address,
                phone=phone
            )
            messages.success(request, 'User added successfully.')
        except Exception as e:
            messages.error(request, f'Failed to add user: {e}')
        
        # Redirect to manage user page
        return redirect('user_list')
    
    # Render form for adding user
    return redirect('user_list')

from django.shortcuts import get_object_or_404

def edit_user(request, user_id):
    # Retrieve the user object or return a 404 error if not found
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        # Extract the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        # Update the user object with the new details
        user.name = name
        user.email = email
        user.address = address
        user.phone = phone
        
        # Save the updated user object
        user.save()
        
        # Redirect to the user list page after successful update
        messages.success(request, 'User updated successfully.')
        return redirect('user_list')
    
    # If the request method is GET, render the edit user form
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('manage_user')  # Redirect to the user list page

def new_car_registration(request):
    if request.method == 'POST':
        car_registration = NewCarRegistration(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        phone_number=request.POST['phone_number'],
        vehicle_number=request.POST['vehicle_number'],
        vehicle_color=request.POST['vehicle_color'],
        model_number=request.POST['model_number'],
        register_name=request.POST['register_name'],
        comment=request.POST['comment']
        )
        car_registration.save()
        # Handle form submission
        return redirect('/thankyou')
    else:
        # For GET requests, show the form or do something else
        return render(request, 'new_car_registration.html')

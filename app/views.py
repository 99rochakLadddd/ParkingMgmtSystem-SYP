from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 




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

# def new_car_registration_view(request):
#     # Your view logic goes here
#     return render(request, 'new_car_registration.html')

def manage_user_view(request):
    return render(request, 'manage_user.html')

# Other view functions remain unchanged
def admin_view(request):
    # Your admin view logic goes here
    return render(request, 'admin_view.html')




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

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
            return redirect('manage_user')
        
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
        return redirect('manage_user')
    
    # Render form for adding user
    return render(request, 'manage_user.html')

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


##new car reg form 
from .models import NewCarRegistration

def new_car_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        vehicle_number = request.POST.get('vehicle_number')
        vehicle_color = request.POST.get('vehicle_color')
        model_number = request.POST.get('model_number')
        register_name = request.POST.get('register_name')
        comment = request.POST.get('comment')

        try:
            NewCarRegistration.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                vehicle_number=vehicle_number,
                vehicle_color=vehicle_color,
                model_number=model_number,
                register_by=register_name,
                comment=comment
            )
            messages.success(request, 'New car registration added successfully.')
        except Exception as e:
            messages.error(request, f'Failed to add new car registration: {e}')

        return redirect('new_car_registration')

    return render(request, 'new_car_registration.html')
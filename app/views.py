from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout  # Import the logout function

def home(request):
    return render(request, "index.html")

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('index')  # Redirect to the login page after successful registration
#     else:
#         initial_data = {'username':'', 'password':'', 'confirm_password':''}
#         form = UserCreationForm(initial=initial_data)
#     return render(request, "register.html", {'form': form})


# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("home")
#     else:
#         form = AuthenticationForm()
#     return render(request, "login.html", {'form': form})

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

from django.shortcuts import render, redirect

def home(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        return redirect("home")
        # print(f"username is {username} and password is {password}")
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        # Extract registration form data
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Perform registration logic (you can save the user in the database, etc.)

        # Redirect to the home page or login page after successful registration
        return redirect("home")

    return render(request, "register.html")

def index_view(request):
    return render(request, 'index.html') 

# while clicking  ew_car_registration button, new_car_registration page from home page will open
def new_car_registration_view(request):
    # Implement your view logic here
    return render(request, 'new_car_registration.html')


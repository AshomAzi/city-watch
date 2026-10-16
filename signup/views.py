from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName", "").strip()
        last_name = request.POST.get("lastName", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirmPassword", "")

        errors = {}

        if not first_name:
            errors["firstName"] = "First name is required"
        if not last_name:
            errors["lastName"] = "Last name is required"
        if not email:
            errors["email"] = "Email is required"
        elif "@" not in email:
            errors["email"] = "Invalid email address"
        if not username:
            errors["username"] = "Username is required"
        if len(password) < 8:
            errors["password"] = "Password must be at least 8 characters long"
        if confirm_password != password:
            errors["confirmPassword"] = "Passwords do not match"

        if email and User.objects.filter(email=email).exists():
            errors["email"] = "Email already exists. Try to login!"

        if username and User.objects.filter(username=username).exists():
            errors["username"] = "Username is already taken!"

        # If there are errors, return the page with old data and error messages
        if errors:
            return render(request, "signup.html", {
                "errors": errors, 
                "old_input": request.POST
            })

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            user.save()
            messages.success(request, f"Account created successfully for {first_name}.")
            return redirect('signin')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return render(request, "signup.html")
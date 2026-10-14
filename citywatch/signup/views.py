from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmPassword")

        if password != confirm_password:
            messages.error(request, "Credentials does not match our records")
            return render(request, "'signup.html")

        if User.objects.filter(username = email).exists():
            messages.error(request, "An account already exist with this email!")
            return render(request, "signin.html")

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name = first_name,
                last_name=last_name,
                password = password,
            )
            user.save()
            messages.success(request, f"Account created successfully for {first_name}.")
            return render(request, "signin.html")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return render(request, "signup.html")
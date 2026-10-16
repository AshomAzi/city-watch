from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def signin(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Credetntials does not match our records")
            return render(request, "signin.html")

    else:
        return render(request, "signin.html")

    
from django.shortcuts import render

# Create your views here.
def badges(request):
    return render(request, "badges.html")
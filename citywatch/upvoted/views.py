from django.shortcuts import render

# Create your views here.
def upvoted(request):
    return render(request, "upvoted.html")
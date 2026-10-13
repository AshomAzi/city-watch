from django.urls import path
from . import views

urlpatterns = [
    path("upvoted/", views.upvoted, name="upvoted")
]
from django.urls import path
from . import views

urlpatterns = [
    path("badges/", views.badges, name="badges")
]
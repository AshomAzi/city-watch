from django.urls import path
from . import views

urlpatterns = [
    path("issues", views.issues, name="issues")
]
from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.aboutpage, name="about"),
]

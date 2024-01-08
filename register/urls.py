from . import views
from django.urls import path

urlpatterns = [
    path('', views.django_register, name="register_user"),

    path('home', views.register_tohome, name="back")   
]
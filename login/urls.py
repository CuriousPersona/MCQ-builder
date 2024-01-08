from . import views
from django.urls import path

urlpatterns = [
    path('', views.django_login, name = 'login_user'),

    path('home', views.django_logout, name="home")
]
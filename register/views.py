from django.shortcuts import render


# Create your views here.
def django_register(request):

    return render(request, 'register/register.html')

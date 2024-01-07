from django.shortcuts import render
from .forms import CourseDetailsForm

# Create your views here.
def django_courseInfo(request):
    display = {"cI_form" : CourseDetailsForm()}

    return render(request, 'courseInfo/courseInfo.html', context = display)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def django_register(request):
    
    if request.method == 'POST':
        # Retrieve data from the faculty details form
        name = request.POST.get('name')
        id_no = request.POST.get('idNo')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone_no = request.POST.get('phoneNo')
        college_name = request.POST.get('collegeName')
        dept_name = request.POST.get('deptName')
        city = request.POST.get('city')
        state = request.POST.get('state')

        # Retrieve data from the account details form
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        faculty = User.objects.create_user(Name = name, IdNo = id_no, DOB = dob, Gender = gender,
                                             PhNo = phone_no, CollegeName = college_name, DeptName = dept_name, 
                                             City = city, State = state, Email = email, Password = password,
                                             ConfirmPwd = confirm_password)
        
        # Check if user with the same email already exists in the database.
        if User.objects.filter(Email=email).exists():
            messages.error(request, 'User with this account already exists. Please use a different account or Login existing account.')
        # returns to the register page 
            return render(request, 'register/register.html')
        
        else :
        # saves user instance
            faculty.save()
            return redirect('courseInfo')
    return render(request, 'register/register.html')

def register_tohome(request):
    render(request, 'home/home.html')



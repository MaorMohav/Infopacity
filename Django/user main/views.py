from django.shortcuts import render
from .models import Manager,Employee,Client

def Login_Page(request):
    return render(request,'Login/Login.html',{})

def Show_Registration(request):
    return render(request,'Register/GeneralRegistration.html',{})

def Show_About(request):
    return render(request,'About/About.html',{})

def Show_Contacts(request):
    return render(request,'Contact/Contact.html',{})

def Show_Manager_Registration(request):
    return render(request,'Register/ManagerRegistration.html',{})

def Show_Employee_Registration(request):
    return render(request,'Register/EmployeeRegistration.html',{})

def Show_Customer_Registration(request):
    return render(request,'Register/CustomerRegistration.html',{})

def Submit_Manager(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    password_conf = request.POST['password_conf']
    email = request.POST['email']
    business_name = request.POST['business_name']
    business_code = request.POST['business_code']

    if password !=password_conf:
        return render(request,'Register/ManagerRegistration.html',{})

    manager= Manager(user_name,password,password_conf,email,business_name,business_code)
    manager.save()

    return render(request, 'Login/Login.html', {})

    
def Submit_Employee(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    password_conf = request.POST['password_conf']
    email = request.POST['email']
    business_name = request.POST['business_name']
    business_code = request.POST['business_code']

    if password !=password_conf:
        return render(request,'Register/EmployeeRegistration.html',{})

    employee= Employee(user_name,password,password_conf,email,business_name,business_code)
    employee.save()

    return render(request, 'Login/Login.html', {})

def Submit_Customer(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    password_conf = request.POST['password_conf']
    email = request.POST['email']

    if password !=password_conf:
        return render(request,'Register/CustomerRegistration.html',{})

    customer= Client(user_name,password,password_conf,email)
    customer.save()

    return render(request, 'Login/Login.html', {})

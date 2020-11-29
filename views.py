from django.shortcuts import render
from .models import Manager,Employee,Client
from django.http import HttpResponse

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

def Show_Regiser_Success(request):
    return render(request,'Register/RegisterSuccess.html',{})

def Show_ManagerHome(request):
    return render(request,'Login/ManagerHome.html',{})

def Check_Password(password,conf_password):
    return not password == conf_password


def isExistsManager(username,email2,businessname,businesscode):
    user = Manager.objects.filter(user_name=username)
    if  user.exists():
        return True

    user = Manager.objects.filter(business_name=businessname)
    if  user.exists():
        return True
    user = Manager.objects.filter(business_code=businesscode)
    if  user.exists():
        return True

    user = Manager.objects.filter(email=email2)
    if  user.exists():
        return True

    return False


def isExistsEmployee(username,email2,businessname,businesscode):
    user = Employee.objects.filter(user_name=username)
    if  user.exists():
        return True

    user = Employee.objects.filter(business_name=businessname)
    if  user.exists():
        return True
    user = Employee.objects.filter(business_code=businesscode)
    if  user.exists():
        return True

    user = Employee.objects.filter(email=email2)
    if  user.exists():
        return True

    return False


def isExistsClient(username,email2):
    user = Client.objects.filter(user_name=username)
    if  user.exists():
        return True

    user = Client.objects.filter(email=email2)
    if  user.exists():
        return True

    return False

def Login_Exists(user_type,username,passw):

    if user_type == 'Manager':
        user = Manager.objects.filter(user_name = username,password = passw)
        if not user.exists():
            return True

    if user_type == 'Employee':
        user = Employee.objects.filter(user_name = username,password = passw)
        if not user.exists():
            return True

    if user_type == 'Client':
        user = Client.objects.filter(user_name = username,password = passw)
        if not user.exists():
            return True

    return False


def Submit_Manager(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']
    email2 = request.POST['email']
    businessname = request.POST['business_name']
    businesscode = request.POST['business_code']

    if Check_Password(passw,passwordconf):
        return render(request,'Register/ManagerRegistration.html',{})

    if isExistsManager(username,email2,businessname,businesscode):
        return render(request,'Register/ManagerRegistration.html',{})

    manager= Manager(user_name = username,password = passw,password_conf=passwordconf,email=email2,business_name= businessname,business_code=businesscode)
    manager.save()

    return render(request, 'Register/RegisterSuccess.html', {})

    
def Submit_Employee(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']
    email2 = request.POST['email']
    businessname = request.POST['business_name']
    businesscode = request.POST['business_code']

    if Check_Password(passw,passwordconf):
        return render(request,'Register/EmployeeRegistration.html',{})

    if isExistsEmployee(username,email2,businessname,businesscode):
        return render(request,'Register/EmployeeRegistration.html',{})
    
    employee= Employee(user_name = username,password = passw,password_conf=passwordconf,email=email2,business_name= businessname,business_code=businesscode)
    employee.save()

    return render(request, 'Register/RegisterSuccess.html', {})

def Submit_Client(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']
    email2 = request.POST['email']


    if Check_Password(passw,passwordconf):
        return render(request,'Register/CustomerRegistration.html',{})

    if isExistsClient(username,email2):
        return render(request,'Register/CustomerRegistration.html',{})

    customer= Client(user_name = username,password = passw,password_conf= passwordconf,email = email2)
    customer.save()

    return render(request, 'Register/RegisterSuccess.html', {})


def Submit_Login(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    user_type = request.POST['duty']

    if Login_Exists(user_type,username,passw):
        return HttpResponse("not exist")

    if user_type == 'Manager':
        return render(request, 'Login/ManagerHome.html', {})

    return HttpResponse("in build")

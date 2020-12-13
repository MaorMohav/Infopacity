from django.shortcuts import render,redirect
from .models import Manager,Client,Employee
from django.http import HttpResponse
from django.contrib.auth import login

##########################################################################################################################
#                                                       SHOW FUNCTIONS                                                   #
##########################################################################################################################

def Login_Page(request):  
    return render(request,'user/Login.html')

def About(request):
    return render(request,'user/About.html')

def Contacts(request):
     return render(request,'user/Contact.html')

def Register(request):
    return render(request,'user/Register.html')

def ManagerRegistration(request):
    return render(request,'user/ManagerRegistration.html')

def EmployeeRegistration(request):
    return render(request,'user/EmployeeRegistration.html')

def ClientRegistration(request):
    return render(request,'user/ClientRegistration.html')

def Regiser_Success(request):
    return render(request,'user/RegisterSuccess.html')

def ManagerHome(request):
    return render(request,'user/ManagerHome.html')

def ManagerUpdate(request):
    return render(request,'user/ManagerPersonal.html')

def EmployeeHome(request):
    return render(request,'user/EmployeeHome.html')

def EmployeeUpdate(request):
    return render(request,'user/EmployeePersonal.html')

def CustomerHome(request):
    return render(request,'user/CustomerHome.html')

def CustomerUpdate(request):
    return render(request,'user/CustomerPersonalUpdate.html')

def ManagerBusinessUpdate(request):
    return render(request,'user/ManagerBusinessUpdate.html')

##########################################################################################################################
#                                                       VERIFY FUNCTIONS                                                 #
##########################################################################################################################

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


##########################################################################################################################
#                                                       SUBMITS AND DATA FUNCTIONS                                       #
##########################################################################################################################

def Submit_Manager(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']
    email2 = request.POST['email']
    businessname = request.POST['business_name']
    businesscode = request.POST['business_code']

    if Check_Password(passw,passwordconf):
        return render(request,'user/ManagerRegistration.html',{})

    if isExistsManager(username,email2,businessname,businesscode):
        return render(request,'user/ManagerRegistration.html',{})

    manager= Manager(user_name = username,password = passw ,email=email2,business_name= businessname,business_code=businesscode)
    manager.save()

    return render(request, 'user/RegisterSuccess.html', {})








def Submit_Employee(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']
    email2 = request.POST['email']
    businessname = request.POST['business_name']
    businesscode = request.POST['business_code']

    if Check_Password(passw,passwordconf):
        return render(request,'user/EmployeeRegistration.html',{})

    if isExistsEmployee(username,email2,businessname,businesscode):
        return render(request,'user/EmployeeRegistration.html',{})
    
    employee= Employee(user_name = username,password = passw,email=email2,business_name= businessname,business_code=businesscode)
    employee.save()

    return render(request, 'user/RegisterSuccess.html', {})







def Submit_Client(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']
    email2 = request.POST['email']


    if Check_Password(passw,passwordconf):
        return render(request,'user/ClientRegistration.html',{})

    if isExistsClient(username,email2):
        return render(request,'user/ClientRegistration.html',{})

    customer= Client(user_name = username,password = passw,email = email2)
    customer.save()

    return render(request, 'user/RegisterSuccess.html', {})




def Submit_Login(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    user_type = request.POST['duty']

    if Login_Exists(user_type,username,passw):
        return HttpResponse("not exist")

    if user_type == 'Manager':
        manager = Manager.objects.filter(user_name= username)
        return render(request, 'user/ManagerHome.html', {'manager':manager})

    if user_type == 'Employee':
        employee = Employee.objects.filter(user_name= username)
        return render(request, 'user/EmployeeHome.html', {'employee':employee})

    if user_type == 'Client':
        client = Client.objects.filter(user_name= username)
        return render(request, 'user/CustomerHome.html', {'client':client})
        

    return HttpResponse("in build")

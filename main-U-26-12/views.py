from django.shortcuts import render,redirect
from .models import Manager,Client,Employee,Business
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

def InsertNumPeople(request):
     return render(request,'user/InsertNumPeople.html')

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


def isExistsManager(username,email2 = None,businessname= None,businesscode= None):
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


def isExistsEmployee(username,email2 = None,businessname = None,businesscode = None):
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


def isExistsClient(username,email2 = None):
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



def businessExists(businessname,businesscode):
    manager =  Manager.objects.filter(business_name= businessname , business_code=businesscode)
    
    if  manager.exists():
            return True

    return False

##########################################################################################################################
#                                                     REGISTER AND LOGIN FUNCTIONS                                       #
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

    business = Business(business_name = businessname,business_code=businesscode,business_manager=username)
    business.save()


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

    if businessExists(businessname,businesscode) == False:
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
        


##########################################################################################################################
#                                                  USER PERSONAL UPDATES FUNCTIONS                                       #
##########################################################################################################################

def ClientEmailUpdate(request):

    username = request.POST['user_name']
    email2 = request.POST['email']

    if isExistsClient(username,email2):
        Client.objects.filter(user_name =username).update(email=email2)
        #client = Client.objects.get(user_name = username)
        #client.email = email2
        #client.save()
        return render(request, 'user/CustomerHome.html')
   
    return render(request, 'user/CustomerHome.html')


def ClientPasswordlUpdate(request):

    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']

    if Check_Password(passw,passwordconf):
        return render(request, 'user/CustomerHome.html')

    if isExistsClient(username):
        Client.objects.filter(user_name =username).update(password=passw)
       # client = Client.objects.get(user_name = username)
        #client.password = passw
        #client.save()
        return render(request, 'user/CustomerHome.html')
    
    return render(request, 'user/CustomerHome.html')



#######################################################################################################################################


def EmployeeEmailUpdate(request):

    username = request.POST['user_name']
    email2 = request.POST['email']

    if isExistsEmployee(username,email2):
        Employee.objects.filter(user_name =username).update(email=email2)
        return render(request, 'user/EmployeeHome.html')
   
    return render(request, 'user/EmployeeHome.html')


def EmployeePasswordlUpdate(request):

    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']

    if Check_Password(passw,passwordconf):
        return render(request, 'user/EmployeeHome.html')

    if isExistsEmployee(username):
        Employee.objects.filter(user_name =username).update(password=passw)
        return render(request, 'user/EmployeeHome.html')
    
    return render(request, 'user/EmployeeHome.html')




#####################################################################################################################################

def ManagerPasswordlUpdate(request):

    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']

    if Check_Password(passw,passwordconf):
       return render(request, 'user/ManagerHome.html')

    if isExistsManager(username):
        Manager.objects.filter(user_name =username).update(password=passw)
        return render(request, 'user/ManagerHome.html')
    
    return render(request, 'user/ManagerHome.html')


def ManagerEmailUpdate(request):

    username = request.POST['user_name']
    email2 = request.POST['email']

    if isExistsManager(username,email2):
        Manager.objects.filter(user_name =username).update(email=email2)
        return render(request, 'user/ManagerHome.html')
   
    return render(request, 'user/ManagerHome.html')


def ManagerBusinessNameUpdate(request):

    username = request.POST['user_name']
    business = request.POST['businessname']

    if isExistsManager(username):
        Manager.objects.filter(user_name =username).update(business_name=business)
        return render(request, 'user/ManagerHome.html')
   
    return render(request, 'user/ManagerHome.html')


def ManagerBusinessCodeUpdate(request):

    username = request.POST['user_name']
    business = request.POST['code']

    if isExistsManager(username):
        Manager.objects.filter(user_name =username).update(business_code=business)
        return render(request, 'user/ManagerHome.html')
   
    return render(request, 'user/ManagerHome.html')

#########################################################################################################################################

def BusinessHours(request):
    username = request.POST['user_name']
    open_h = request.POST['opening']
    close_h = request.POST['closing']

    if isExistsManager(username):
        Business.objects.filter(business_manager =username).update(opening=open_h,closing = close_h)
        return render(request, 'user/ManagerHome.html')


    return render(request, 'user/ManagerHome.html')


def BusinessCapacity(request):
    username = request.POST['user_name']
    capacityy = request.POST['capacity']
   
    if isExistsManager(username):
        Business.objects.filter(business_manager =username).update(capacity=capacityy)
        return render(request, 'user/ManagerHome.html')


    return render(request, 'user/ManagerHome.html')


def BusinessDescription(request):
    username = request.POST['user_name']
    desc = request.POST['description']
   
    if isExistsManager(username):
        Business.objects.filter(business_manager =username).update(description=desc)
        return render(request, 'user/ManagerHome.html')


    return render(request, 'user/ManagerHome.html')

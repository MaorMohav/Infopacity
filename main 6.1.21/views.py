from django.shortcuts import render,redirect
from .models import Manager,Employee,Client,Business,Business_inside,number_of_customers,customer,queue_customer
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
        obj1="error"
        return render(request, 'user/ManagerRegistration.html', {'obj1':obj1})

    if isExistsManager(username,email2,businessname,businesscode):
        obj1="error"
        return render(request, 'user/ManagerRegistration.html', {'obj1':obj1})

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
        obj1="error"
        return render(request, 'user/EmployeeRegistration.html', {'obj1':obj1})

    if isExistsEmployee(username,email2,businessname,businesscode):
        obj1="error"
        return render(request, 'user/EmployeeRegistration.html', {'obj1':obj1})

    if businessExists(businessname,businesscode) == False:
        obj1="error"
        return render(request, 'user/EmployeeRegistration.html', {'obj1':obj1})

    employee= Employee(user_name = username,password = passw,email=email2,business_name= businessname,business_code=businesscode)
    employee.save()

    return render(request, 'user/RegisterSuccess.html', {})







def Submit_Client(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    passwordconf = request.POST['password_conf']
    email2 = request.POST['email']


    if Check_Password(passw,passwordconf):
        obj1="error"
        return render(request, 'user/ClientRegistration.html', {'obj1':obj1})

    if isExistsClient(username,email2):
        obj1="error"
        return render(request, 'user/ClientRegistration.html', {'obj1':obj1})


    customer= Client(user_name = username,password = passw,email = email2)
    customer.save()

    return render(request, 'user/RegisterSuccess.html', {})




def Submit_Login(request):
    username = request.POST['user_name']
    passw = request.POST['password']
    user_type = request.POST['duty']

    if Login_Exists(user_type,username,passw):
        obj1="error"
        return render(request, 'user/Login.html', {'obj1':obj1})

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
    city1 = request.POST.get('city',False)
    desc = request.POST['description']
   
    if isExistsManager(username):
        Business.objects.filter(business_manager =username).update(description=desc, city = city1)
        return render(request, 'user/ManagerHome.html')


    return render(request, 'user/ManagerHome.html')

########################################################################################################################################
#                                                          QUEUE MANEGMENT                                                             #
########################################################################################################################################

def check_serial(businesscode):
    user = Employee.objects.filter(business_code=businesscode)
    if  user.exists():
        return True

    return False

def check_number(businesscode):
    user = number_of_customers.objects.filter(business_code=businesscode)
    if  user.exists():
        return True

    return False

def Start_queue(request):

    initial = request.POST.get('initialize',False)
    businesscode = request.POST['business_code']
    


    if check_serial(businesscode) == True:
        if Business_inside.objects.filter(business_code = businesscode).exists() == False:
            business= Business_inside(number_of_people = initial,business_code= businesscode)
            business.save()


        if check_number(businesscode) == False:
            number1 =  number_of_customers(number_of_people = initial,business_code= businesscode)
            number1.save()
        
        else:
            number1 = number_of_customers.objects.get(business_code = businesscode)
            number1.number_of_people += int(initial)
            number1.save()
            obj2 =Business_inside.objects.get(business_code = businesscode)
      #      if obj2.number_of_people != 0:
        #        obj2.number_of_people +=int(initial)
          #      obj2.save()
           # else:
            #    obj2.number_of_people =int(initial)
             #   obj2.save()

    if queue_customer.objects.filter(business_code = businesscode).exists() == True:
        obj = queue_customer.objects.all()
        obj2 =Business_inside.objects.get(business_code = businesscode)
        return render(request,'user/InsertNumPeople.html',{'number_of_people':obj2 , 'obj':obj})

    obj2 =Business_inside.objects.get(business_code = businesscode)
    
    return render(request,'user/InsertNumPeople.html',{'number_of_people':obj2 })

def Add_to_queue(request):

    name_p = request.POST['name']
    businesscode = request.POST['business_code']
    number = request.POST['amount']

    number1 = number_of_customers.objects.get(business_code = businesscode)
    
    if Business_inside.objects.filter(business_code = businesscode).exists() == True:
        if  check_number(businesscode) == True:
            queue = queue_customer(name = name_p, number_of_people=number,business_code=businesscode)
            queue.save()

            obj = queue_customer.objects.all()
            obj2 =Business_inside.objects.get(business_code = businesscode)
            return render(request,'user/InsertNumPeople.html',{'number_of_people':obj2,'obj':obj } )

    obj2 =Business_inside.objects.get(business_code = businesscode)
    return render(request,'user/InsertNumPeople.html',{'number_of_people':obj2})


def Remove_from_queue(request):

    name_p = request.POST['name1']
    businesscode = request.POST['business_code']
    number = request.POST['amount']

    if queue_customer.objects.filter(business_code = businesscode).exists() == True:
        if queue_customer.objects.filter(name = name_p).exists() == True:
            obj1 =  queue_customer.objects.get(name = name_p)
            if obj1.number_of_people - int(number) <= 0:
                obj1.delete()
                obj2 =Business_inside.objects.get(business_code = businesscode)
                obj2.number_of_people +=int(number)
                obj2.save()
                number1 = number_of_customers.objects.get(business_code = businesscode)
                number1.number_of_people += int(number)
                number1.save()

            else:
                obj1.number_of_people -= int(number)
                obj1.save()
                number1 = number_of_customers.objects.get(business_code = businesscode)
                number1.number_of_people += int(number)
                number1.save()
                obj2 =Business_inside.objects.get(business_code = businesscode)
                obj2.number_of_people +=int(number)
                obj2.save()

    obj = queue_customer.objects.all()
    obj2 =Business_inside.objects.get(business_code = businesscode)

    return render(request,'user/InsertNumPeople.html',{'number_of_people':obj2 , 'obj':obj})

    



            
def Reset_queue(request):

    businesscode = request.POST['business_code']

    
    obj = Business_inside.objects.get(business_code=businesscode)
    obj.number_of_people = 0
    obj.save()
    Business_inside.objects.all().delete()
    queue_customer.objects.all().delete()

    
    return render(request,'user/InsertNumPeople.html')


def Delete_business(request):

    businesscode = request.POST['business_code']
    number = request.POST['amount']

    obj2 =Business_inside.objects.get(business_code = businesscode)
    
    if obj2.number_of_people-int(number) > 0:
        obj2.number_of_people -=int(number)
        obj2.save()

    else:
        obj2.number_of_people = int(0)
        obj2.save()


    obj = queue_customer.objects.all()


    return render(request,'user/InsertNumPeople.html',{'number_of_people':obj2 , 'obj':obj})


##########################################################################################################################################
#                                                              Search
#########################################################################################################################################

def ClientSearch(request):

    b_name = request.POST['user_name']
    city1 = request.POST['city']



    if  Business.objects.filter(city = city1, business_name=b_name).exists() == True :
        obj1 =Business.objects.get(business_name = b_name ,city= city1)
        if Business_inside.objects.filter(business_code=obj1.business_code).exists() == True:
            business = Business_inside.objects.get(business_code=obj1.business_code)
            return render(request,'user/CustomerResults.html',{'obj1':obj1, 'business':business})
        else:
            business = None
            return render(request,'user/CustomerResults.html',{'obj1':obj1, 'business':business})

    elif  city1 != 'All cities':
        if city1 != None and Business.objects.filter(city = city1).exists() == True:
            obj2 = Business.objects.filter(city = city1)
            obj1 = None
            obj3 = Business_inside.objects.all()
            obj4 = []

            for i in obj2:
                if Business_inside.objects.filter(business_code = i.business_code).exists() == True:
                    obj4.append(i.business_code)

            return render(request,'user/CustomerResults.html', {'obj2':obj2 ,'obj1':obj1, 'obj3':obj3 ,'obj4':obj4})

        elif b_name != None and Business.objects.filter(business_name=b_name).exists() == True :
            obj1 = Business.objects.get(business_name = b_name)
            if Business_inside.objects.filter(business_code=obj1.business_code).exists() == True:
                business = Business_inside.objects.get(business_code=obj1.business_code)
                return render(request,'user/CustomerResults.html',{'obj1':obj1, 'business':business})
            else:
                business = None
                return render(request,'user/CustomerResults.html',{'obj1':obj1, 'business':business})

    
   
    return render(request,'user/CustomerHome.html')


def EmployeeSearch(request):

    b_name = request.POST['user_name']
    city1 = request.POST['city']



    if  Business.objects.filter(city = city1, business_name=b_name).exists() == True :
        obj1 =Business.objects.get(business_name = b_name ,city= city1)
        if Business_inside.objects.filter(business_code=obj1.business_code).exists() == True:
            business = Business_inside.objects.get(business_code=obj1.business_code)
            return render(request,'user/EmployeeResults.html',{'obj1':obj1, 'business':business})
        else:
            business = None
            return render(request,'user/EmployeeResults.html',{'obj1':obj1, 'business':business})

    elif  city1 != 'All cities':
        if city1 != None and Business.objects.filter(city = city1).exists() == True:
            obj2 = Business.objects.filter(city = city1)
            obj1 = None
            obj3 = Business_inside.objects.all()
            obj4 = []

            for i in obj2:
                if Business_inside.objects.filter(business_code = i.business_code).exists() == True:
                    obj4.append(i.business_code)

            return render(request,'user/EmployeeResults.html', {'obj2':obj2 ,'obj1':obj1, 'obj3':obj3 ,'obj4':obj4})

        elif b_name != None and Business.objects.filter(business_name=b_name).exists() == True :
            obj1 = Business.objects.get(business_name = b_name)
            if Business_inside.objects.filter(business_code=obj1.business_code).exists() == True:
                business = Business_inside.objects.get(business_code=obj1.business_code)
                return render(request,'user/EmployeeResults.html',{'obj1':obj1, 'business':business})
            else:
                business = None
                return render(request,'user/EmployeeResults.html',{'obj1':obj1, 'business':business})

    
   
    return render(request,'user/EmployeeHome.html')


def ManagerSearch(request):

    b_name = request.POST['user_name']
    city1 = request.POST['city']



    if  Business.objects.filter(city = city1, business_name=b_name).exists() == True :
        obj1 =Business.objects.get(business_name = b_name ,city= city1)
        if Business_inside.objects.filter(business_code=obj1.business_code).exists() == True:
                business = Business_inside.objects.get(business_code=obj1.business_code)
                return render(request,'user/ManagerResults.html',{'obj1':obj1, 'business':business})
        else:
            business = None
            return render(request,'user/ManagerResults.html',{'obj1':obj1, 'business':business})

    elif  city1 != 'All cities':
        if city1 != None and Business.objects.filter(city = city1).exists() == True:
            obj2 = Business.objects.filter(city = city1)
            obj1 = None
            obj3 = Business_inside.objects.all()
            obj4 = []

            for i in obj2:
                if Business_inside.objects.filter(business_code = i.business_code).exists() == True:
                    obj4.append(i.business_code)

            return render(request,'user/ManagerResults.html', {'obj2':obj2 ,'obj1':obj1, 'obj3':obj3 ,'obj4':obj4})

        elif b_name != None and Business.objects.filter(business_name=b_name).exists() == True :
            obj1 = Business.objects.get(business_name = b_name)
            if Business_inside.objects.filter(business_code=obj1.business_code).exists() == True:
                business = Business_inside.objects.get(business_code=obj1.business_code)
                return render(request,'user/ManagerResults.html',{'obj1':obj1, 'business':business})
            else:
                business = None
                return render(request,'user/ManagerResults.html',{'obj1':obj1, 'business':business})

    
   
    return render(request,'user/ManagerHome.html')
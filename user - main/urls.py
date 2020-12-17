from django.urls import path
from django.conf.urls import url, include
from user import views
from .models import Manager,Employee,Client

app_name = 'user'

urlpatterns = [
    path('',views.Login_Page,name = "Login"),
    path('About/',views.About,name = "About"),
    path('Contact/',views.Contacts,name = "Contact"),
    path('Register/',views.Register,name = "Register"),
    path('Register/Manager/',views.ManagerRegistration,name = "ManagerRegistration"),
    path('Register/Employee/',views.EmployeeRegistration,name = "EmployeeRegistration"),
    path('Register/Client/',views.ClientRegistration,name = "ClientRegistration"),
    path('Register/success/',views.Regiser_Success,name="RegisterSuccess"),
    path('ManagerHome/',views.ManagerHome,name="ManagerHome"),
    url(r'^Manager/',views.Submit_Manager,name ="Submit_Manager"),
    url(r'^Employee/',views.Submit_Employee,name ="Submit_Employee"),
    url(r'^Customer/',views.Submit_Client,name ="Submit_Customer"),
    path('user/',views.Submit_Login,name ="User_Login"),
    path('manager/update/',views.ManagerUpdate,name="ManagerUpdate"),
    path('EmployeeHome/',views.EmployeeHome,name = "EmployeeHome"),
    path('employee/update/',views.EmployeeUpdate,name="EmployeeUpdate"),
    path('CustomerHome/',views.CustomerHome,name = "CustomerHome"),
    path('customer/update/',views.CustomerUpdate,name="CustomerUpdate"),
    path('manager/update/business/',views.ManagerBusinessUpdate,name="ManagerBusinessUpdate"),
    url(r'^customer/update/personalEmail/',views.ClientEmailUpdate,name="ClientEmailUpdate"),
    url(r'^customer/update/personalPassword/',views.ClientPasswordlUpdate,name="ClientPasswordUpdate"),
    url(r'^employee/update/personalEmail/',views.EmployeeEmailUpdate,name="EmployeeEmailUpdate"),
    url(r'^employee/update/personalPassword/',views.EmployeePasswordlUpdate,name="EmployeePasswordUpdate"),
    url(r'^manager/update/personalPassword/',views.ManagerPasswordlUpdate,name="ManagerPasswordUpdate"),
    url(r'^manager/update/personalEmail/',views.ManagerEmailUpdate,name="ManagerEmailUpdate"),
    url(r'^manager/update/personalBusineesname/',views.ManagerBusinessNameUpdate,name="ManagerBusinessNameUpdate"),
    url(r'^manager/update/personalBusineescode/',views.ManagerBusinessCodeUpdate,name="ManagerBusinessCodeUpdate"),
    url(r'^manager/update/business/hours',views.BusinessHours,name="Businesshours"),
    url(r'^manager/update/business/maxcapacity',views.BusinessCapacity,name="Businesscapacity"),
    url(r'^manager/update/business/description',views.BusinessDescription,name="Businessdescription"),
]

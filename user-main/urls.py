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
]

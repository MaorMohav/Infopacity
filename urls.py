from django.urls import path
from django.conf.urls import url, include
from user import views

app_name = 'user'

urlpatterns = [
   path('Login/', views.Login_Page,name ="Login"),
   path('Login/ManagerHome',views.Show_ManagerHome,name="ManagerHome"),
   url(r'^About/',views.Show_About,name ="About"),
   url(r'^Contact',views.Show_Contacts,name ="Contact"),
   url(r'^Register/',views.Show_Registration,name ="Register"),
   path('ManagerRegistration/',views.Show_Manager_Registration,name ="ManagerRegistration"),
   path('EmployeeRegistration/',views.Show_Employee_Registration,name ="EmployeeRegistration"),
   path('CustomerRegistration/',views.Show_Customer_Registration,name ="CustomerRegistration"),
   path('Register/success/',views.Show_Regiser_Success,name="RegisterSuccess"),
   url(r'^Manager/',views.Submit_Manager,name ="Submit_Manager"),
   url(r'^Employee/',views.Submit_Employee,name ="Submit_Employee"),
   url(r'^Customer/',views.Submit_Client,name ="Submit_Customer"),
   url(r'Login/id',views.Submit_Login,name ="User_Login"),
   
]
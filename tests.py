
from django.test import TestCase
from .models import Manager, Employee, Client
from user import views
import unittest

class URLTests(TestCase):
    #check urls of a local server pages 

    #check login page
    def test_Login_Page(self):
        response = self.client.get('Login/')
        self.assertEqual(response.status_code, 404)

    #check Register page
    def test_Register_Page(self):
        response = self.client.get('Register/')
        self.assertEqual(response.status_code, 404)

    #check General Register page
    def test_general_Register_Page(self):
        response = self.client.get('GeneralRegister/')
        self.assertEqual(response.status_code, 404)

    #check Manager Register page
    def test_ManagerRegister_Page(self):
        response = self.client.get('Register/Manager/')
        self.assertEqual(response.status_code, 404)

     #check Employee Register page
    def test_EmployeeRegister_Page(self):
        response = self.client.get('Register/Employee/')
        self.assertEqual(response.status_code, 404)

    #check Customer Register page
    def test_CustomRegister_Page(self):
        response = self.client.get('Register/Client/')
        self.assertEqual(response.status_code, 404)

    #check About page
    def test_About_Page(self):
        response = self.client.get('About/')
        self.assertEqual(response.status_code, 404)

    #check Contact page
    def test_Contact_Page(self):
        response = self.client.get('Contact/')
        self.assertEqual(response.status_code, 404)


    def test_Login_Page(self):
        response = self.client.get('Login/')
        self.assertEqual(response.status_code, 404)


    def test_GeneralRegister_Page(self):
        response = self.client.get('Register/')
        self.assertEqual(response.status_code, 404)


    def test_Register_success_Page(self):
        response = self.client.get('Register/success/')
        self.assertEqual(response.status_code, 404)

    def test_Managerhome_Page(self):
        response = self.client.get('ManagerHome/')
        self.assertEqual(response.status_code, 404)


    def test_EmployeeHome_Page(self):
        response = self.client.get('EmployeeHome/')
        self.assertEqual(response.status_code, 404)


    def test_CustomerHome_Page(self):
        response = self.client.get('CustomerHome/')
        self.assertEqual(response.status_code, 404)


    def test_CustomerUpdate_Page(self):
        response = self.client.get('customer/update/')
        self.assertEqual(response.status_code, 404)

    def test_ManagerUpdate_Page(self):
        response = self.client.get('manager/update/')
        self.assertEqual(response.status_code, 404)

    def test_CustomerUpdate_Page(self):
        response = self.client.get('customer/update/')
        self.assertEqual(response.status_code, 404)    


class Views_Test(TestCase):
   
    #check Check_Password function
    def test_check_password(self):
        self.assertEquals(False,views.Check_Password(111111,111111))
        self.assertEquals(True,views.Check_Password(123456,1444467))

    
    
    
    
    
     # check isExistsManager function
    def test_Manager_is_exists(self):
        user = Manager(user_name = 'Ariel',password = '123456',email='Ariel@gmail.com',business_name='Infopacity',business_code='32168421')
        user.save()
        self.assertTrue(True,views.isExistsManager('Ariel','Ariel@gmail.com','Infopacity','32168421'))
        self.assertFalse(False,views.isExistsManager('Maor','Ariel@gmail.com','Infopacity','32168421'))

    
    
    
    
     # check isExistsEmployee function
    def test_Employee_is_exists(self):
        user = Employee(user_name = 'Maor',password = '123456',email='Maor@gmail.com',business_name='Infopacity',business_code='32168421')
        user.save()
        self.assertTrue(True,views.isExistsEmployee('Maor','Maor@gmail.com','Infopacity','32168421'))
        self.assertFalse(False,views.isExistsEmployee('Ariel','Ariel@gmail.com','Infopacity','32168421'))
    




    # check isExistsClient function
    def test_Client_is_exists(self):
        user = Client(user_name = 'Sergey',password = '123456',email='Sergey@gmail.com')
        user.save()
        self.assertTrue(True,views.isExistsClient('Maor','Sergey@gmail.com'))
        self.assertFalse(False,views.isExistsClient('Vlad','Vlad@gmail.com'))

    
    
    
    # check Login_Exists function
    def test_Login(self):                                                                                                
       self.assertFalse(False,views.Login_Exists('Client','Sergey','13456'))
       self.assertTrue(True,views.Login_Exists('Manager','Ariel','123456'))
       self.assertTrue(True,views.Login_Exists('Employee','Maor','123456'))
       self.assertFalse(False,views.Login_Exists('Client','Vlad','13456'))
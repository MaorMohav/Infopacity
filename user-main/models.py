from django.db import models

class Manager(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    business_code = models.CharField(max_length=50)

    def __str__(self):
        return f'user_name: {self.user_name}, password: {self.password}, email: {self.email}, business_name: {self.business_name}, business_code: {self.business_code} '
    

class Employee(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    business_code = models.CharField(max_length=50)

    def __str__(self):
        return f'user_name: {self.user_name}, password: {self.password},email: {self.email}, business_name: {self.business_name}, business_code: {self.business_code} '

class Client(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'user_name: {self.user_name}, password: {self.password}, email: {self.email}'




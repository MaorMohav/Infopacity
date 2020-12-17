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


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    business_code = models.CharField(max_length=50)
    business_manager = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    opening = models.CharField(max_length=5)
    closing = models.CharField(max_length=5)
    capacity = models.CharField(max_length=50)

    def __str__(self):
        return f'business_name: {self.business_name}, business_code: {self.business_code}, business_manager: {self.business_manager} ,description: {self.description}, opening: {self.opening}, closing: {self.closing} , capacity: {self.capacity} '
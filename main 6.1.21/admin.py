from django.contrib import admin


from .models import *

admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Business)
admin.site.register(number_of_customers)
admin.site.register(customer)
admin.site.register(Business_inside)
admin.site.register(queue_customer)

# Register your models here.

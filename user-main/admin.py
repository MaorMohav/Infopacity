from django.contrib import admin


from .models import Manager,Employee,Client

admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Client)

# Register your models here.

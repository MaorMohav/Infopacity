from django.contrib import admin


from .models import Manager,Employee,Client,Business

admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Business)

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import Job, Employee

admin.site.register(Job)
admin.site.register(Employee)

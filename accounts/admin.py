from django.contrib import admin
from .models import Student, Employer, University

# Register your models here.
admin.site.register(Student)
admin.site.register(Employer)
admin.site.register(University)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'num_cert')

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_org', 'email', 'initials')

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
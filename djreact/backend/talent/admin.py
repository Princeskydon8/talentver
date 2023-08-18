from django.contrib import admin
from .models import Company, Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_registration", "registration_number", "contact_person", "number_of_employees")
    list_filter = ("date_of_registration",)
    search_fields = ("name", "registration_number", "contact_person", "email_address")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "department", "role", "date_started", "date_left")
    list_filter = ("company", "department", "role")
    search_fields = ("name", "employee_id", "department", "role")

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)

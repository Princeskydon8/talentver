from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    date_of_registration = models.DateField()
    registration_number = models.CharField(max_length=50)
    address = models.TextField()
    contact_person = models.CharField(max_length=100)
    departments = models.TextField()
    number_of_employees = models.PositiveIntegerField()
    contact_phone = models.CharField(max_length=15)
    email_address = models.EmailField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()

    def __str__(self):
        return self.name

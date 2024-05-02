from django.db import models


class Plan(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    STATUS_CHOICES = [
        (ACTIVE, 'ACTIVE'),
        (INACTIVE, 'INACTIVE'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    validity_days = models.CharField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    adhar_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(auto_now_add=True)
    assigned_mobile_number = models.CharField(max_length=10)
    plan = models.ForeignKey(Plan, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

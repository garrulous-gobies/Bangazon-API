from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateField(null=True, blank=True)
    isSupervisor = models.BooleanField(default=False)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='department')

    def __str__(self):
        return f'{self.lastName}, {self.firstName}'

    class Meta:
        ordering = ('lastName',)

class Department(models.Model):
    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class PaymentType(models.Model):
    name = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    # customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='customer')

    def __str__(self):
        return f'{self.name}, {self.accountNumber}'
from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateField(null=True, blank=True)
    isSupervisor = models.BooleanField(default=False)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='department')
    computer = models.ManyToManyField('Computer', through="Employee_Computer", related_name='employees')

    def __str__(self):
        return f'{self.lastName}, {self.firstName}'

    class Meta:
        ordering = ('lastName',)

class Department(models.Model):
    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Computer(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    purchaseDate = models.DateField(null=True, blank=True)
    decommissionDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self


class Employee_Computer(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)
    assign_date = models.DateField(null=True, blank=True)
    unassign_date = models.DateField(null=True, blank=True)

    @property
    def current_assignment(self):
        if self.assign_date != None and self.unassign_date == None :
            return True
        else:
            return False

    def __str__(self):
        return self


class PaymentType(models.Model):
    name = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    # customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='customer')

    def __str__(self):
        return f'{self.name}, {self.accountNumber}'

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()
    # customer = models.ForeignKey()
    productType = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True, related_name='productType')

    def __str__(self):
        return f'{self.title}'

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

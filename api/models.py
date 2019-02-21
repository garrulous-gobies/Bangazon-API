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

class Customer(models.Model):
    """ Defines an customer (effectively a user)
        Author: Brendan McCray
        Methods: __str__ returns all fields (last name, first name, street_address, city, state, zipcode, and phone_number)
    """

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return f"{self.lastName}, {self.firstName}, {self.street_address}, {self.city}, {self.state}, {self.zipcode}, {self.phone_number}"

    class Meta:
        ordering = ('lastName',)

class PaymentType(models.Model):
    name = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=False, related_name='customer')

    def __str__(self):
        return f'{self.name}, {self.accountNumber}'

class Order(models.Model):
    """ Defines an order
        Author: Brendan McCray
        Methods: __str__ returns all fields (customer last name, first name, payment_type, and payment_date)
    """

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT, default=None, null=True, blank=True)
    payment_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.id}, {self.customer.firstName} {self.customer.lastName}, {self.payment_type.name if self.payment_type else None} {self.payment_date}"

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

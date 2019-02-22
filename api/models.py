from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateField(null=True, blank=True)
    isSupervisor = models.BooleanField(default=False)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='department')

    @property
    def current_computer(self):
        current_computer = Employee_Computer.objects.get(employee=self, unassign_date=None)

        if current_computer:
            return current_computer
        else:
            return None

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
    date_joined = models.DateField(default=None, null=True, blank=True)
    date_deleted = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.lastName}, {self.firstName}, {self.street_address}, {self.city}, {self.state}, {self.zipcode}, {self.phone_number}"

    class Meta:
        ordering = ('lastName',)


class Computer(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    purchaseDate = models.DateField(null=True, blank=True)
    decommissionDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.model}, {self.manufacturer}'


class Employee_Computer(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)
    assign_date = models.DateField(null=True, blank=True)
    unassign_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'unassign_date: {self.unassign_date}'


class PaymentType(models.Model):
    name = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=False, related_name="customer_payment")

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


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, default=None, null=True, blank=True)
    productType = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name='productType')

    def __str__(self):
        return f'{self.title}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, null=True, blank=True)
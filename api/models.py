from django.db import models

class Employee(models.Model):
    """Defines an employee and includes a getter property that evaluates whether the employee has a computer assigned or not

       Authors: Brendan McCray, Nolan Little, Austin Zoradi, Zac Jones

       Methods: __str__ returns lastName and firstName
    """

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateField(null=True, blank=True)
    isSupervisor = models.BooleanField(default=False)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

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
    """Defines a department

       Authors: Brendan McCray, Nolan Little, Austin Zoradi, Zac Jones

       Methods: __str__ returns department name
    """

    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    """ Defines an customer (effectively a user)

        Author: Brendan McCray

        Methods: __str__ returns all fields
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

    @property
    def has_placed_order(self):
        order = Order.objects.filter(customer=self)
        if len(order) == 0:
            order = False
        else:
            order = True
        return order

    def __str__(self):
        return f"{self.lastName}, {self.firstName}, {self.street_address}, {self.city}, {self.state}, {self.zipcode}, {self.phone_number}"

    class Meta:
        ordering = ('lastName',)


class Computer(models.Model):
    """Defines a computer

       Author: Nolan Little

       Methods: __str__ returns computer model and manufacturer
    """

    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    purchaseDate = models.DateField(null=True, blank=True)
    decommissionDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.model}, {self.manufacturer}'


class Employee_Computer(models.Model):
    """Defines an employee and includes a getter property that evaluates whether the employee has a computer assigned or not

       Authors: Nolan Little, Brendan McCray

       Methods: __str__ returns unassign date of computer
    """

    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)
    assign_date = models.DateField(null=True, blank=True)
    unassign_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'unassign_date: {self.unassign_date}'


class PaymentType(models.Model):
    """Defines an employee and includes a getter property that evaluates whether the employee has a computer assigned or not

       Author: Austin Zoradi

       Methods: __str__ returns name and account number
    """

    name = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=False, related_name="customer_payment")

    def __str__(self):
        return f'{self.name}, {self.accountNumber}'


class Order(models.Model):
    """ Defines an order

        Author: Brendan McCray

        Methods: __str__ returns all fields (payment type and date will return None if null)
    """

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT, default=None, null=True, blank=True)
    payment_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.id}, {self.customer.firstName} {self.customer.lastName}, {self.payment_type.name if self.payment_type else None} {self.payment_date if self.payment_date else None}"


class ProductType(models.Model):
    """Defines a product type

       Author: Austin Zoradi

       Methods: __str__ retuns name of product type
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """Defines a product, which is sold by a customer and can may or may not be associated with one or more orders

       Author: Zac Jones

       Methods: __str__ returns title of product
    """

    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, default=None, null=True, blank=True)
    productType = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name='productType')

    def __str__(self):
        return f'{self.title}'

class OrderProduct(models.Model):
    """Defines a join table explicitly for products that exist on a given order

       Author: Brendan McCray

       Methods: __str__ returns order and product information, respectively
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.order} {self.product}'

class TrainingProgram(models.Model):
    name = models.CharField(max_length=50)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    maxAttendees = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class EmployeeTrainingProgram(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    trainingProgram = models.ForeignKey(TrainingProgram, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.employee} {self.trainingProgram}'

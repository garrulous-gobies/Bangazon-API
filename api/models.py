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
    purchaseDate = models.DateField()
    decommissionDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self


class Employee_Computer(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)
    dateAssigned = models.DateField(null=True, blank=True)

    def __str__(self):
        return self
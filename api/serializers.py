from rest_framework import serializers
from api.models import *

class EmployeeInDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """Used with the DepartmentSerializer to nest employee information within each department when the proper url extension is provided

    Authors: Brendan McCray
    """

    class Meta:
      model = Employee
      fields = ('id','firstName','lastName','startDate','isSupervisor','url')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        super(DepartmentSerializer, self).__init__(*args, **kwargs)

        request = kwargs['context']['request']
        include = request.query_params.get('_include')

        # note related name of department on Employee model
        if include == 'employees':
            self.fields['employees'] = EmployeeInDepartmentSerializer(source='employee_set', many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id','name','budget','url')


class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        fields = ('id','model','manufacturer','purchaseDate','decommissionDate','url')


class EmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):
    computer = ComputerSerializer()

    class Meta:
        model = Employee_Computer
        fields=('assign_date', 'computer')


class EmployeeDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """Used with EmployeeSerializer to display department name in Employee resource (list and detail view)

    Author: Brendan McCray
    """

    class Meta:
        model = Department
        fields = ('id','name','url')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """Used to display a list view of employees or a detail view of a specific employee

    Authors: Brendan McCray, Nolan Little, Austin Zoradi, Zac Jones
    """

    # nests department name and in each employee
    department = EmployeeDepartmentSerializer(read_only=True)
    # nests current computer within each employee (null if no current computer exixts)
    current_computer = EmployeeComputerSerializer(read_only=True)

    class Meta:
      model = Employee
      fields = ('id', 'firstName', 'lastName', 'startDate', 'isSupervisor', 'department', 'current_computer','url')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

  def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)

        request = kwargs['context']['request']
        include = request.query_params.get('_include')

        if include == 'products':
            self.fields['products'] = ProductSerializer(source='product_set', many=True, read_only=True)

        elif include == 'payments':
            self.fields['payment_types'] = PaymentTypeSerializer(source='customer_payment', many=True, read_only=True)

  class Meta:
    model = Customer
    fields = ('id','firstName','lastName','street_address','city','state','zipcode','phone_number','date_joined','date_deleted','url')


class CustomerOnOrderSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Customer
    fields = ('id','firstName','lastName','street_address','city','state','zipcode','phone_number','date_joined','date_deleted','url')


class OrderSerializer(serializers.HyperlinkedModelSerializer):

  def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)

        request = kwargs['context']['request']
        include = request.query_params.get('_include')

        if include == 'products':
            self.fields['products'] = OrderProductSerializer(source='orderproduct_set', many=True, read_only=True)

        if include == 'customers':
            self.fields['customer'] = CustomerOnOrderSerializer(read_only=True)

  class Meta:
    model = Order
    fields = ('id','payment_date','customer','payment_type','url')


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = ('id','name','accountNumber','customer','url')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('id','title','price','description','quantity','customer','productType','url')


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ('product',)


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'url', 'name')


class EmployeeTrainingProgramSerializer(serializers.HyperlinkedModelSerializer):

  employee = EmployeeSerializer()

  class Meta:
    model = EmployeeTrainingProgram
    fields = ('employee',)

class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
  """Used with the EmployeeTrainingProgram to nest employee information within each training program

  Authors: Zac Jones, Austin Zoradi
  """

  employee = EmployeeTrainingProgramSerializer(source='employeetrainingprogram_set', many=True, read_only=True)

  class Meta:
    model = TrainingProgram
    fields = ('id','name', 'startDate', 'endDate', 'maxAttendees', 'employee','url')

class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    '''Used to display a detail view of orders and have the product details of each order also appear

    Authors: Austin Zoradi, Nolan Little
    '''

    product = OrderProductSerializer(source='orderproduct_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'url', 'customer', 'payment_type', 'payment_date', 'product')

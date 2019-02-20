from rest_framework import serializers
from api.models import *

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Department
    fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
  department = DepartmentSerializer()

  class Meta:
    model = Employee
    fields = ('firstName','lastName','startDate','isSupervisor','department')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Customer
    fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Order
    fields = '__all__'

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = '__all__'
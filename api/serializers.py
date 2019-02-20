from rest_framework import serializers
from api.models import *

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Department
    fields = '__all__'

class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        fields = '__all__'

class EmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee_Computer
        fields='__all__'
        depth = 1

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
  department = DepartmentSerializer()
  computer = ComputerSerializer()

  class Meta:
    model = Employee
    fields = ('firstName','lastName','startDate','isSupervisor','department', 'computer')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = '__all__'

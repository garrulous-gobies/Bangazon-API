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

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
from rest_framework import serializers
from api.models import *
from rest_framework import serializers 

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Department
    fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
  department = DepartmentSerializer()

  class Meta:
    model = Employee
    fields = ('firstName','lastName','startDate','isSupervisor','department')
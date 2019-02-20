from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import filters

from api.models import *
from api.serializers import *

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'employees': reverse('employees', request=request, format=format),
        'departments': reverse('departments', request=request, format=format)
    })

class EmployeeViewSet(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer
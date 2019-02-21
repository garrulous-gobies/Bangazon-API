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

  def get_queryset(self):
    query_set = Department.objects.all()
    keyword = self.request.query_params.get('_include', '_filter=budget&_gt', None)
    if keyword is '_include':
      print("query params", keyword)
      query_set = query_set.filter(name__icontains=keyword)
    elif keyword is '_filter=budget&_gt':
        print("query params", keyword)
        query_set = query_set.filter(bugdet__gt=keyword)
    else:
        print("NOne???????????????????????????????????????????????????", keyword)
    return query_set

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
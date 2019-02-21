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
        'departments': reverse('departments', request=request, format=format),
        'computers': reverse('computers', request=request, format=format)
    })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer
  http_method_names = ['get', 'post', 'put']

  def get_queryset(self):
    query_set = Department.objects.all()

    keyword = self.request.query_params.get('_include')
    if keyword is not None:
        print("query params_________", keyword)
        query_set = query_set.filter(name__icontains=keyword)

    keyword = self.request.query_params.get('_filter')
    if keyword == 'budget':
        keyword = self.request.query_params.get('_gt')
        if keyword is not None:
            print("query params", keyword)
            query_set = query_set.filter(budget__gt=keyword)

    return query_set


  

class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

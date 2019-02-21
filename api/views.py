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
    '''Summary: Can view departments and department details. Can search in url with "?_include=employees" to view all employees in each department department. Can search for departments with budgets greater than a certain number with "?_filter=budget&_gt=  ". 
    
    Verbs supported: GET, POST, PUT
    
    Author(s): Austin Zoradi, Roger Brondon McCray, Nolan Little, Zac Jones
    '''


    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post', 'put']

    def get_queryset(self):
        query_set = Department.objects.all()

        keyword = self.request.query_params.get('_filter')
        if keyword == 'budget':

            keyword = self.request.query_params.get('_gt')
            if keyword is not None:
                query_set = query_set.filter(budget__gt=keyword)

        return query_set


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    '''Summary: ViewSet for payment types. Can view all payment types and details. 

    Verbs supported: GET, POST, PUT, DELETE
    
    Author(s): Ausitn Zoradi
    '''

    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    '''Summary: ViewSet for product types. Can view all product types and details. 

    Verbs supported: GET, POST, PUT, DELETE
    
    Author(s): Ausitn Zoradi
    '''
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

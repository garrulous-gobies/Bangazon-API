from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from api.models import *
from api.serializers import *
import datetime

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'employees': reverse('employees', request=request, format=format),
        'departments': reverse('departments', request=request, format=format),
        'customers': reverse('customers', request=request, format=format),
        'orders': reverse('orders', request=request, format=format),
        'computers': reverse('computers', request=request, format=format)
    })

class EmployeeViewSet(viewsets.ModelViewSet):
    '''Summary: Can view employees and employee details.

    Verbs supported: GET, POST, PUT, PATCH, DELETE

    Author(s): Austin Zoradi, Brendan McCray, Nolan Little, Zac Jones
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    '''Summary: Can view departments and department details. Can search in url with "?_include=employees" to view all employees in each department. Can search for departments with budgets greater than a certain number with "?_filter=budget&_gt=  ".

    Verbs supported: GET, POST, PUT

    Author(s): Austin Zoradi, Brendan McCray, Nolan Little, Zac Jones
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



class CustomerViewSet(viewsets.ModelViewSet):
    '''Summary: ViewSet for list of all Customers or a single Customer. If the query string parameter of ?_include=products, or ?_include=payments is provided then the appropriate data will be returned nested in the response. if ?q={search param} is provided the customer fields will be searched for the search paramater and the filtered response returned.

    Verbs supported: GET, POST, PUT, DELETE

    Author(s): Brendan McCray
    '''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'put']

    def get_queryset(self):
        query_set = self.queryset
        print('query params', self.request.query_params)

        # search all parameters of each customer based on the params provided
        keyword = self.request.query_params.get('q')
        if keyword is not None:
            query_set = query_set.filter(Q(firstName__icontains=keyword) | Q(lastName__icontains=keyword) | Q(street_address__icontains=keyword) | Q(city__icontains=keyword) | Q(state__icontains=keyword) | Q(zipcode__icontains=keyword) | Q(phone_number__icontains=keyword))

        keyword = self.request.query_params.get('active')
        if keyword == 'false' or keyword == 'False':
            query_set = [cust for cust in query_set if cust.has_placed_order == False]

        return query_set


class OrderViewSet(viewsets.ModelViewSet):
    '''Summary: ViewSet for Orders. Can view all orders in a list view, and the order detail with product details appended on as well.

    Verbs supported: GET, POST, PUT, DELETE

    Author(s): Ausitn Zoradi, Brendan McCray, Nolan Little
    '''

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        else:
            return OrderSerializer

    queryset = Order.objects.all()

    def get_queryset(self):
        query_set = self.queryset

        # search all parameters of each customer based on the params provided
        keyword = self.request.query_params.get('completed')
        if keyword == 'True' or keyword == 'true':
            query_set = query_set.exclude(payment_type__isnull=True)
        elif keyword == 'False' or keyword == 'false':
            query_set = query_set.exclude(payment_type__isnull=False)
        else:
          pass

        return query_set


class ComputerViewSet(viewsets.ModelViewSet):
    '''ViewSet for Computers. Can view all computers or a single instance of a computer

    Verbs supported: GET, POST, PUT, DELETE

    Author(s): Nolan Little
    '''

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    '''Summary: ViewSet for payment types. Can view all payment types and details.

    Verbs supported: GET, POST, PUT, DELETE

    Author(s): Austin Zoradi
    '''

    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''ViewSet for Products. Can view all products or a single instance of a Product

    Verbs supported: GET, POST, PUT, DELETE

    Author(s): Zac Jones
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    '''Summary: ViewSet for product types. Can view all product types and details.

    Verbs supported: GET, POST, PUT, DELETE

    Author(s): Austin Zoradi
    '''
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class TrainingProgramViewSet(viewsets.ModelViewSet):
    '''Summary: ViewSet for trainings.

    Verbs supported: GET, POST, PUT, DELETE

    Author(s): Zac Jones
    '''
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer

    def get_queryset(self):
      current_date = datetime.date.today()
      query_set = TrainingProgram.objects.all()
      keyword = self.request.query_params.get('completed')

      if keyword == 'true':
        query_set = query_set.filter(endDate__lt=current_date)
      elif keyword == 'false':
        query_set = query_set.filter(endDate__gte=current_date)
      return query_set

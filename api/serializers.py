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

  def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)

        request = kwargs['context']['request']
        include = request.query_params.get('_include')

        if include == 'products':
            self.fields['products'] = ProductSerializer(source='product_set', many=True, read_only=True)

        if include == 'payments':
            self.fields['payment_types'] = PaymentTypeSerializer(source='customer_payment', many=True, read_only=True)

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

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'url', 'name')

from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)
router.register('computers', views.ComputerViewSet)
router.register('paymentType', views.PaymentTypeViewSet)
router.register('productType', views.ProductTypeViewSet)
router.register('product', views.ProductViewSet)
router.register('trainingProgram', views.TrainingProgramViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls))
]
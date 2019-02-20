from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('computers', views.ComputerViewSet)
router.register('employee_computers', views.EmployeeComputerViewSet)
router.register('paymentType', views.PaymentTypeViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls))
]
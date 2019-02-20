from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls))
]
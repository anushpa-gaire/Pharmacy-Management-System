from django.urls import path
from apps.customer.api.views import CustomerView, UpdateCustomerView

urlpatterns = [
    path('', CustomerView.as_view()),
    path('<int:id>/', UpdateCustomerView.as_view()),
]
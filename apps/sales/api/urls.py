from django.urls import path
from apps.sales.api.views import SalesView

urlpatterns = [
    path('', SalesView.as_view()),
]
from django.urls import path
from apps.medicine.api.views import MedicineView

urlpatterns = [
    path('',MedicineView.as_view())
]
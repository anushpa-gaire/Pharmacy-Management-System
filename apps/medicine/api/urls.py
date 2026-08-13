from django.urls import path
from apps.medicine.api.views import MedicineView, UpdateMedicineView

urlpatterns = [
    path('',MedicineView.as_view()),
    path('<int:id>', UpdateMedicineView.as_view())
]
from django.urls import path
from apps.pharmacy.api.views import PharmacyView, UpdatePharmacyView

urlpatterns = [
    path('',PharmacyView.as_view()),
    path('<int:id>', UpdatePharmacyView.as_view())
]
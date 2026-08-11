from django.urls import path

from apps.pharmacy.views import (PharmacyCreateView, PharmacyDeleteView,
                                 PharmacyDetailView, PharmacyListView,
                                 PharmacyUpdateView)

urlpatterns = [
    path("list/", PharmacyListView.as_view(), name="pharmacy_list"),
    path("create/", PharmacyCreateView.as_view(), name="pharmacy_create"),
    path(
        "update/<int:pk>", PharmacyUpdateView.as_view(), name="pharmacy_update"
    ),
    path(
        "delete/<int:pk>", PharmacyDeleteView.as_view(), name="pharmacy_delete"
    ),
    path(
        "detail/<int:pk>", PharmacyDetailView.as_view(), name="pharmacy_detail"
    ),
]
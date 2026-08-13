from django.urls import path
from apps.supplier.views import (
    SupplierList,
    SupplierCreate,
    SupplierUpdate,
    SupplierDelete,
    SupplierDetail,
)

urlpatterns = [
    path("supplier_list/", SupplierList.as_view(), name="supplier_list"),
    path("supplier_create/", SupplierCreate.as_view(), name="supplier_create"),
    path("supplier_update/<int:pk>", SupplierUpdate.as_view(), name="supplier_update"),
    path("supplier_delete/<int:pk>", SupplierDelete.as_view(), name="supplier_delete"),
    path("supplier_detail/<int:pk>", SupplierDetail.as_view(), name="supplier_detail"),
]
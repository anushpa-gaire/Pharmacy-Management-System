from django.urls import path
from apps.supplier.api.views import supplier_delete, supplier_list, supplier_create, supplier_update

urlpatterns = [
    path('list',supplier_list, name="supplier-list"),
    path('create',supplier_create, name="supplier-create"),
    path('update/<int:id>',supplier_update, name="supplier-update"),
    path('delete/<int:id>',supplier_delete, name="supplier-delete"),
]
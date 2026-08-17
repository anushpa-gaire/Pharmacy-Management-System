from django.urls import path
from apps.inventory.api.views import InventoryView

urlpatterns = [
    path("", InventoryView.as_view(), name="inventory")
]
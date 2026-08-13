from django.urls import path

from apps.purchase.api.views import (
    PurchaseView,
    UpdatePurchaseView,
)

urlpatterns = [
    path("", PurchaseView.as_view()),
    path("<int:id>/", UpdatePurchaseView.as_view()),
]
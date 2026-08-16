from django.urls import path

from apps.purchase.api.views import (
    PurchaseView,
    UpdatePurchaseView,
    verify_purchase,
)

urlpatterns = [
    path("", PurchaseView.as_view()),
    path("<int:id>/", UpdatePurchaseView.as_view()),
    path('verify_purchase/<int:id>', verify_purchase),
]
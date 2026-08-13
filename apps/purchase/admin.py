from django.contrib import admin
from apps.purchase.models import Purchase, PurchaseItem

# Register your models here.

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "purchase_number",
        "supplier",
        "purchase_date",
        "total",
        "payment_status",
    )

    search_fields = (
        "purchase_number",
        "invoice_number",
    )

    list_filter = (
        "payment_status",
        "purchase_date",
    )


@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = (
        "purchase",
        "medicine",
        "batch_number",
        "quantity",
        "total",
    )

    search_fields = (
        "batch_number",
        "medicine__name",
    )
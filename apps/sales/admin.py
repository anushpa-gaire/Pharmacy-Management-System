from django.contrib import admin
from .models import Sales, SalesItem


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_number",
        "customer",
        "sub_total",
        "discount",
        "tax",
        "total",
        "payment_status",
        "payment_method",
        "created_at",
    )

    list_filter = (
        "payment_status",
        "payment_method",
        "created_at",
    )

    search_fields = (
        "invoice_number",
        "customer__name",
    )

    readonly_fields = ("created_at",)

    ordering = ("-created_at",)


@admin.register(SalesItem)
class SalesItemAdmin(admin.ModelAdmin):
    list_display = (
        "sale",
        "medicine",
        "batch",
        "quantity",
        "unit_price",
        "discount",
        "tax",
        "total",
    )

    list_filter = (
        "medicine",
        "batch",
    )

    search_fields = (
        "medicine__name",
        "sale__invoice_number",
    )
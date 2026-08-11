from django.contrib import admin
from apps.supplier.models import Supplier

# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        "company_name",
        "contact_person",
        "email",
        "phone",
        "status",
        "created_at",
    ]

    list_filter = [
        "status",
        "created_at",
    ]

    search_fields = [
        "company_name",
        "contact_person",
        "email",
        "registration_number",
    ]

    ordering = ["company_name"]
    readonly_fields = [
        "created_at",
        "updated_at"
    ]

    fieldsets = [
        ["Company Information", {
            "fields": [
                "company_name",
                "contact_person",
                "registration_number",
                "status",
            ]
        }],
        ["Contact Information", {
            "fields": [
                "email",
                "phone",
                "address",
            ]
        }],
        ["Payment Details", {
            "fields": [
                "payment_terms",
            ]
        }],
        ["System Information", {
            "fields": [
                "created_at",
                "updated_at",
            ]
        }]
    ]
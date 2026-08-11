from django.contrib import admin
from .models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        "medicine_code",
        "name",
        "generic_name",
        "brand_name",
        "dosage_form",
        "strength",
        "selling_price",
        "purchase_price",
        "reorder_level",
        "expiry_date",
        "status",
    )

    list_filter = (
        "status",
        "dosage_form",
        "manufacture_date",
        "expiry_date",
        "created_at",
    )

    search_fields = (
        "name",
        "generic_name",
        "brand_name",
        "medicine_code",
        "barcode",
    )

    ordering = ("name",)
    list_per_page = 25
    date_hierarchy = "created_at"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Medicine Information",
            {
                "fields": (
                    ("name", "medicine_code"),
                    ("generic_name", "brand_name"),
                    ("dosage_form", "strength"),
                    "barcode",
                )
            },
        ),
        (
            "Pricing",
            {
                "fields": (
                    ("purchase_price", "selling_price"),
                    "tax_rate",
                )
            },
        ),
        (
            "Inventory",
            {
                "fields": (
                    "reorder_level",
                    "storage_location",
                    ("manufacture_date", "expiry_date"),
                    "status",
                )
            },
        ),
        (
            "System Information",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )
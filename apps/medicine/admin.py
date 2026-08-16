from django.contrib import admin
from .models import Catgeory, Medicine, MedicineBatch


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        "medicine_code",
        "name",
        "generic_name",
        "brand_name",
        "dosage_form",
        "strength",
        "reorder_level",
        "status",
    )

    list_filter = (
        "status",
        "dosage_form",
        "manufacture_date",
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
            "Inventory",
            {
                "fields": (
                    "reorder_level",
                    "storage_location",
                    "status","category"
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


admin.site.register(Catgeory)



@admin.register(MedicineBatch)
class MedicineBatchAdmin(admin.ModelAdmin):
    list_display = (
        "medicine",
        "batch_number",
        "supplier",
        "quantity",
        "purchase_price",
        "selling_price",
        "manufacturing_date",
        "expiry_date",
        "received_date",
        "status",
    )

    list_filter = (
        "status",
        "supplier",
        "expiry_date",
        "received_date",
    )

    search_fields = (
        "medicine__name",
        "batch_number",
        "supplier__name",
    )

    list_editable = (
        "quantity",
        "selling_price",
        "status",
    )


    ordering = (
        "-received_date",
        "medicine",
        "batch_number",
    )

    date_hierarchy = "received_date"

    fieldsets = (
        (
            "Medicine & Batch",
            {
                "fields": (
                    "medicine",
                    "batch_number",
                    "supplier",
                )
            },
        ),
        (
            "Stock & Pricing",
            {
                "fields": (
                    "quantity",
                    "purchase_price",
                    "selling_price",
                    "status",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "manufacturing_date",
                    "expiry_date",
                    "received_date",
                )
            },
        ),
    )
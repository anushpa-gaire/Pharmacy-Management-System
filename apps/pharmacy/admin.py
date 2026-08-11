from django.contrib import admin
from .models import District, Pharmacy


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("district_id", "name")
    search_fields = ("name",)
    ordering = ("district_id",)


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "registration_number",
        "email",
        "phone",
        "city",
        "district",
        "status",
        "opening_time",
        "closing_time",
        "created_at",
    )
    list_filter = ("status", "district", "city", "created_at")
    search_fields = (
        "name",
        "registration_number",
        "email",
        "phone",
        "city",
    )
    ordering = ("name",)
    list_per_page = 20

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "name",
                "registration_number",
                "email",
                "phone",
                "website",
            )
        }),
        ("Location", {
            "fields": (
                "address",
                "city",
                "district",
            )
        }),
        ("Business Hours", {
            "fields": (
                "opening_time",
                "closing_time",
            )
        }),
        ("Status", {
            "fields": ("status",)
        }),
    )

    readonly_fields = ("created_at", "updated_at")
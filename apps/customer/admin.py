from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Columns shown in the list overview view
    list_display = ("id", "full_name", "phone", "email", "date_of_birth", "status", "created_at")
    
    # Clickable fields to open the edit page
    list_display_links = ("id", "full_name")
    
    # Sidebar filters for quick pharmacy sorting
    list_filter = ("status", "gender", "created_at")
    
    # Search box functionality for pharmacists to find patients instantly
    search_fields = ("full_name", "phone", "email")
    
    # Read-only fields that the pharmacist cannot manually modify
    readonly_fields = ("created_at", "updated_at")
    
    # Form layout inside the individual customer record view
    fieldsets = (
        ("Personal Information", {
            "fields": ("full_name", "date_of_birth", "gender")
        }),
        ("Contact Details", {
            "fields": ("phone", "email", "address", "emergency_contact")
        }),
        ("System Details", {
            "fields": ("status", "created_at", "updated_at")
        }),
    )

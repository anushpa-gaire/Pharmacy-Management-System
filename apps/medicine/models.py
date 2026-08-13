from django.db import models

# Create your models here.
class Catgeory(models.Model):
    name = models.CharField(max_length=10, verbose_name="Catgeory Name")
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "catgeory"

class DosageForm(models.TextChoices):
    TABLET = "tablet", "Tablet"
    CAPSULE = "capsule", "Capsule"
    SYRUP = "syrup", "Syrup"
    INJECTION = "injection", "Injection"
    CREAM = "cream", "Cream"
    OINTMENT = "ointment", "Ointment"
    DROPS = "drops", "Drops"
    INHALER = "inhaler", "Inhaler"
    POWDER = "powder", "Powder"
    GEL = "gel", "Gel"
    LOTION = "lotion", "Lotion"
    SUSPENSION = "suspension", "Suspension"
    SOLUTION = "solution", "Solution"
    SPRAY = "spray", "Spray"
    SUPPOSITORY = "suppository", "Suppository"
    PATCH = "patch", "Patch"
    LOZENGE = "lozenge", "Lozenge"
    GRANULES = "granules", "Granules"
    SHAMPOO = "shampoo", "Shampoo"
    MOUTHWASH = "mouthwash", "Mouthwash"
    EYE_DROPS = "eye_drops", "Eye Drops"
    EAR_DROPS = "ear_drops", "Ear Drops"
    NASAL_DROPS = "nasal_drops", "Nasal Drops"
    NASAL_SPRAY = "nasal_spray", "Nasal Spray"
    IV_FLUID = "iv_fluid", "IV Fluid"


class MedicineStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"
    OUT_OF_STOCK = "out_of_stock", "Out of Stock"
    DISCONTINUED = "discontinued", "Discontinued"
    EXPIRED = "expired", "Expired"

class Medicine(models.Model):
    name = models.CharField(max_length=80, verbose_name="Medicine Name")
    generic_name = models.CharField(max_length=100, blank=True)
    brand_name = models.CharField(max_length=100, blank=True)
    medicine_code = models.IntegerField(unique=True)
    category = models.ForeignKey(Catgeory, on_delete=models.CASCADE, null=True, blank=True)
    dosage_form = models.CharField(max_length=20, choices=DosageForm.choices, default=DosageForm.TABLET)
    strength = models.CharField(max_length=10, help_text="store mg/mcg/IU/mL of medicine")
    barcode = models.PositiveIntegerField(unique=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.IntegerField(default=10)
    storage_location  = models.CharField(max_length=150, null=True, blank=True)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=15, choices=MedicineStatus.choices, default=MedicineStatus.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        db_table = "medicine"
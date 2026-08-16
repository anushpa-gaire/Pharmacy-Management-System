from django.db import models
from apps.medicine.models import Medicine
from apps.supplier.models import Supplier

# Create your models here.

class PaymentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    PAID = 'paid', 'Paid'
    UNPAID = 'unpaid', 'Unpaid'

class Purchase(models.Model):
    purchase_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    invoice_number = models.CharField(max_length=50, null=True, blank=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_purchase_verified = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return self.purchase_number


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=50)
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    class Meta:
        db_table = 'purchase_item'

    def __str__(self):
        return f"{self.purchase.purchase_number} - {self.medicine.name}"
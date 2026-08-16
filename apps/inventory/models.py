from django.db import models

# Create your models here.
class TransactionType(models.TextChoices):
    PURCHASE = "purchase", "Purchase"
    SALE = "sale", "Sale"
    SALE_RETURN = "sale_return", "Sale Return"
    PURCHASE_RETURN = "purchase_return", "Purchase Return"
    DAMAGE = "damage", "Damage"
    EXPIRY = "expiry", "Expiry"
    MANUAL_ADJUSTMENT = "manual_adjustment", "Manual Adjustment"
    STOCK_TRANSFER = "stock_transfer", "Stock Transfer"


class InventoryTxn(models.Model):
    batch = models.ForeignKey('medicine.MedicineBatch', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=30, choices=TransactionType.choices)
    quantity = models.PositiveIntegerField()
    reference_id = models.CharField(max_length=20, null=True, blank=True)
    previous_stock = models.PositiveIntegerField()
    new_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.transaction_type}'

    class Meta:
        db_table = "inventory_txn"
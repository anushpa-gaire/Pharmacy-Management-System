
from apps.inventory.api.service import create_inventory_txn
from apps.medicine.models import MedicineBatch
from apps.inventory.models import InventoryTxn, TransactionType

def create_medicine_batch(**kwargs):
    medicine = kwargs.get('medicine')
    batch_number = kwargs.get('batch_number')
    manufacturing_date = kwargs.get('manufacturing_date')
    expiry_date = kwargs.get('expiry_date')
    purchase_price = kwargs.get('purchase_price')
    selling_price = kwargs.get('selling_price')
    supplier = kwargs.get('supplier')
    quantity = kwargs.get('quantity')
    received_date = kwargs.get('received_date','2022-02-02')

    data = MedicineBatch.objects.create(
        medicine = medicine,
        batch_number = batch_number,
        manufacturing_date = manufacturing_date,
        expiry_date = expiry_date,
        quantity = quantity,
        purchase_price = purchase_price,
        selling_price = selling_price,
        supplier = supplier,
        received_date = received_date,
        status = True
    )
    create_inventory_txn(
        batch_number = data,
        txn_type = TransactionType.PURCHASE,
        qty = quantity,
        reference_id = f'REF-{supplier.company_name[:3]}-{data.id}',
        previous_stock = 0,
        new_stock = quantity,
    )

    return data
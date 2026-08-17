from apps.inventory.models import InventoryTxn

def create_inventory_txn(**kwargs):
    batch = kwargs.get('batch_number')
    transaction_type = kwargs.get('txn_type')
    qty = kwargs.get('qty')
    reference_id = kwargs.get('reference_id')
    previous_stock = kwargs.get('previous_stock')
    new_stock = kwargs.get('new_stock')

    inv = InventoryTxn.objects.create(
        batch = batch,
        transaction_type = transaction_type,
        quantity = qty,
        reference_id = reference_id,
        previous_stock = previous_stock,
        new_stock = new_stock
    )

    return inv
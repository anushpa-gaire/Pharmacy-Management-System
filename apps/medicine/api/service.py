def create_medicine_batch(**kwargs):
    medicine = kwargs.get('medicine')
    manufacturing_date = kwargs.get('manufacturing_date')
    expiry_date = kwargs.get('expiry_date')
    purchase_price = kwargs.get('purchase_price')
    selling_price = kwargs.get('selling_price')
    supplier = kwargs.get('supplier')
    received_date = kwargs.get('received_date','2022-02-02')
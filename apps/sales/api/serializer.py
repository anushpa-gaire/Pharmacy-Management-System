from datetime import datetime, date

from rest_framework import serializers
from rest_framework.validators import ValidationError

from apps.medicine.models import MedicineBatch
from apps.sales.models import Sales, SalesItem
from django.db import transaction


class SalesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesItem
        fields = ["quantity", "unit_price", "discount", "tax", "medicine", "batch"]

    def validate_batch(self, batch):
        if batch.expiry_date <= date.today():
            raise ValidationError("Medicine batch is expired.")
        return batch

    def validate(self, attrs):
        medicine = attrs['medicine']
        batch = attrs['batch']
        earlier_batch = MedicineBatch.objects.filter(
            medicine=medicine,
            expiry_date__gt=date.today(),
            expiry_date__lt=batch.expiry_date,
        ).exists()

        if earlier_batch:
            raise ValidationError(
                "Use the earlier expiring batch for this medicine."
            )
        return attrs



class SalesSerializer(serializers.ModelSerializer):
    sales_item = SalesItemSerializer(many=True, write_only=True)

    class Meta:
        model = Sales
        fields = ["invoice_number", "customer", "payment_method", "sales_item"]

    @transaction.atomic
    def create(self, validated_data):
        sales_item = validated_data.pop("sales_item")
        discount = 0
        sub_total = 0
        tax = 0

        for item in sales_item:
            sub_total += item["unit_price"] * item["quantity"]
            discount += item["discount"]
            tax += item["tax"]
        total = sub_total - discount + tax
        validated_data["discount"] = discount
        validated_data["sub_total"] = sub_total
        validated_data["tax"] = tax
        validated_data["total"] = total
        sale = Sales.objects.create(**validated_data)

        for item in sales_item:
            SalesItem.objects.create(sale=sale, **item)

        return sale
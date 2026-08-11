from rest_framework import serializers

from apps.medicine.models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        exclude = ['purchase_price']
from rest_framework import serializers
from apps.medicine.models import Catgeory, Medicine

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catgeory
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category_name']=instance.category.name
        return data
from rest_framework import serializers
from apps.supplier.models import Supplier
from rest_framework.validators import ValidationError


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


    def validate_company_name(self, company_name):
        if len(company_name)<3:
            raise ValidationError("Company name should be greater than 3")
        return company_name


    def validate_email(self,email):
        data = Supplier.objects.filter(email=email).exists()
        if data:
            raise ValidationError("Email should be unique")
        return email
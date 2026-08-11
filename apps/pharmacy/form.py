from django import forms
from apps.pharmacy.models import Pharmacy

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = "__all__"
from django import forms
from productions.models import Production

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        exclude = []

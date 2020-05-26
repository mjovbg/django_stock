from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        # fields in your form - it will go into db:
        fields = ['ticker']





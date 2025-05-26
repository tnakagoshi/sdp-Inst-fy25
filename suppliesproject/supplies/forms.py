from django import forms
from .models import Rental  # Replace with your actual model name

class RentalModelForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['quantity', 'start_date', 'end_date']
        widgets = {
           'start_date': forms.DateInput(attrs={'type': 'date'}),
           'end_date':   forms.DateInput(attrs={'type': 'date'}),
        }

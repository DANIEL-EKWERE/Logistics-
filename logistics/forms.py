from django import forms
from .models import GetQuote

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = GetQuote
        fields = ['firstName', 'lastName', 'business', 'email', 'phone']

class AddressForm(forms.ModelForm):
    class Meta:
        model = GetQuote
        fields = ['address1', 'address2', 'city', 'state', 'postalCode', 'date', 'time']

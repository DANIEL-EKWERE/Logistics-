from django import forms
from .models import GetQuote
from datetime import datetime
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = GetQuote
        fields = ['firstName', 'lastName', 'business', 'email', 'phone']

class AddressForm(forms.ModelForm):
    class Meta:
        model = GetQuote
        fields = ['address1', 'address2', 'city', 'state', 'postalCode', 'date', 'time']



class QuoteForm(forms.Form):
    firstName = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'First Name'
    }))
    lastName = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Last Name'
    }))
    business = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Business / Organization'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number'
    }))
    address1 = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Address Line 1'
    }))
    address2 = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Address Line 2'
    }))
    city = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'City'
    }))
    state = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'State/Province/Region'
    }))
    postalCode = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Postal Code'
    }))


    # Setting the min attribute for date and time fields with seconds
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M')

    date = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'type': 'date',
        'min':current_date,
    }))
    time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={
        'type': 'time',
        'min':current_time,
    }))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, error_messages={'required':'complete the reCaptcha and try resubmitting the form again'}, required=True)

    class Meta:
        model = GetQuote
        fields = ('firstName','lastName','email','phone','bussiness','address1','address2','city','state','postalCode','date','time','captcha')

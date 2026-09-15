"""Django forms for Family Wedding Centre."""

from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    """Customer enquiry / contact form."""

    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Full Name',
            'autocomplete': 'name',
        }),
        error_messages={'required': 'Please enter your name.'},
    )

    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Phone Number',
            'autocomplete': 'tel',
            'inputmode': 'tel',
        }),
        error_messages={'required': 'Please enter your phone number.'},
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address (optional)',
            'autocomplete': 'email',
        }),
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input form-textarea',
            'placeholder': 'Tell us about your requirements...',
            'rows': 5,
        }),
        error_messages={'required': 'Please enter a message.'},
    )

    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email', 'message']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits = ''.join(c for c in phone if c.isdigit())
        if len(digits) < 7:
            raise forms.ValidationError('Please enter a valid phone number.')
        return phone

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Please enter your full name.')
        return name

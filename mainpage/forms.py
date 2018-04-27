from django import forms
from django.core import validators


class RegisterEmail(forms.Form):
    form_name = forms.CharField(required=True, label='your name')
    form_email = forms.EmailField(required=True, label='Your email')
    bot_detector = forms.CharField(required=False, widget=forms.HiddenInput,
                                   validators=[validators.MaxLengthValidator(0)])

from django import forms
from .models import *
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.http.request import HttpRequest

class Contact_form(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'email_contact', 'text']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'name': 'name', 'id': 'name', 'placeholder': 'نام و نام خانوادگی'}),
            'email_contact': forms.EmailInput(
                attrs={'class': 'form-control', 'name': 'email', 'id': 'email', 'placeholder': 'ایمیل'}),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'name': 'note', 'id': 'note', 'placeholder': 'پیام'})
        }
        error_messages = {
            'name': {
                'max_length':'اشتباه وارد کردی عزیزم',
                'required': 'مثل بچه ادم فیلد ها رو پر کن'
            }
        }

class Contact_form_en(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'light', 'data-language': 'en', 'dir': 'ltr'}))
    class Meta:
        model = Contact
        fields = ['name', 'email_contact', 'text']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'name': 'name', 'id': 'name', 'placeholder': 'name'}),
            'email_contact': forms.EmailInput(
                attrs={'class': 'form-control', 'name': 'email', 'id': 'email', 'placeholder': 'email'}),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'name': 'note', 'id': 'note', 'dir': 'rtl', 'placeholder': 'text'})
        }


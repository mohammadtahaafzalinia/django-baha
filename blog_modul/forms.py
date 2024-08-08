from django.forms import forms
from django_recaptcha.fields import *
class contact_form(forms.Form):
    captcha=ReCaptchaField()
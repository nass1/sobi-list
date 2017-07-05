from django import forms
from django.forms import ModelForm, Textarea
from . models import About
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField, StrictButton, FormActions
from captcha.fields import CaptchaField

class AboutForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = About
        exclude = ['approved_published',]

        widgets = {
                'description': Textarea(attrs={'cols': 80, 'rows': 20}),
                'brief_description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class CatoForm(ModelForm):
    class Meta:
        model = About
        fields = ['country']

from django import forms
from django.forms import ModelForm, Textarea
from . models import About



class AboutForm(ModelForm):
    model = About
    fields = '__all__'
    widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'brief_description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

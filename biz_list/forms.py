from django import forms
from django.forms import ModelForm, Textarea
from . models import About
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField, StrictButton, FormActions

class AboutForm(ModelForm):
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





class CustomerListFormHelper(FormHelper):

    form_id = 'customer-search-form'
    form_class = 'form-inline'
    #field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    helper = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Customer Records',
                    InlineField('dealer_account_number'),
                    InlineField('customer_last_name'),
                    InlineField('customer_first_name'),
                    InlineField('primary_phone'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search',
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )

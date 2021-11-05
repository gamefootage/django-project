""" Define forms in checkout app """
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ Define OrderForm """
    class Meta:
        """ Configure meta for OrderForm """
        model = Order
        fields = ('full_name', 'email', 'phone',
                  'street_address1', 'street_address2',
                  'city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form fields """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'country': 'Country',
            'postcode': 'Post Code',
            'city': 'City/Town',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Personal Details',
                Div(
                    'full_name',
                    css_class = 'col'
                ),
                Div(
                    'email',
                    css_class = 'col'
                ),
                Div(
                    'phone',
                    css_class = 'col'
                ),
                css_class = 'row'
            ),
            Fieldset(
                'Delivery Details',
                Div(
                    Div(
                        Div(
                            'street_address1',
                            css_class="col"
                        ),
                        Div(
                            'street_address2',
                            css_class="col"
                        ),
                        Div(
                            'city',
                            css_class="col"
                        ),
                        css_class="row"
                    ),
                    Div(
                        Div(
                            'county',
                            css_class="col"
                        ),
                        Div(
                            'country',
                            css_class="col"
                        ),
                        Div(
                            'postcode',
                            css_class="col"
                        ),
                        css_class="row"
                    ),
                    css_class="col-12"
                ),
                css_class="row"
            ),
        )

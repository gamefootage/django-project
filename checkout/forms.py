""" Define forms in checkout app """
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, HTML, Submit
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
                    Div(
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
                    css_class = 'col'
                )
            ),
            Fieldset(
                'Delivery Details',
                Div(
                    Div(
                        Div(
                            'street_address1',
                            css_class="col"
                        )
                    ),
                    Div(
                        Div(
                            'street_address2',
                            css_class="col"
                        )
                    ),
                    Div(
                        Div(
                            'city',
                            css_class="col"
                        ),
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
            HTML("""
                <div class="row">
                    <div class="col-12 text-end">
                        {% if user.is_authenticated %}
                            <label for="id-save-info">
                            Save this delivery information to my profile
                            </label>
                            <input class="stripe-style-input ms-2" type="checkbox" id="id-save-info" name="save-info" checked>
                        {% else %}
                            <label class="form-check-label" for="id-save-info">
                                <a class="text-info" href="{% url 'account_signup' %}">Create an account</a> or 
                                <a class="text-info" href="{% url 'account_login' %}">login</a> to save this information
                            </label>
                        {% endif %}
                    </div>
                </div>
                <fieldset class="row">
                    <legend>Payment</legend>
                    <div class="col-12 px-5">
                        <!-- Stripe Card Element -->
                        <div class="mb-3" id="payment-element"></div>

                        <!-- Stripe Errors -->
                        <div class="mb-3 text-danger" id="error-message" role="alert"></div>
                    </div>
                </fieldset>
            """),
            Submit(
                'submit-payment', 'Pay €{{cart_total}}',
                css_class="btn btn-success float-end"
            )
        )

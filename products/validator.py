"""Custom JSON Validator"""
from cerberus import Validator
from django.core.exceptions import ValidationError

def validate_quantity(value):
    """Validate quantity field for products.Product model"""
    schema = {
        's': {'type': 'integer'},
        'm': {'type': 'integer'},
        'l': {'type': 'integer'}
    }
    custom_validator = Validator(schema)

    if not custom_validator.validate(value):
        raise ValidationError(
            f'{value} is not of valid schema'
        )

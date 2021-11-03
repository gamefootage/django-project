from cerberus import Validator
from django.core.exceptions import ValidationError

def validate_quantity(value):
    schema = {'s': {'type': 'integer'}, 'm': {'type': 'integer'}, 'l': {'type': 'integer'}}
    v = Validator(schema)

    if not v.validate(value):
        raise ValidationError(
            f'{value} is not of valid schema'
        )
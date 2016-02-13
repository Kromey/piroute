import re


from django import forms
from django.core.exceptions import ValidationError


from . import validators


class IPNetworkField(forms.Field):
    ipv4_masked_network_re = re.compile(r'^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}/\d{1,3}(\.\d{1,3}){3}\Z')
    default_validators = [validators.validate_ipv4_network]

    def to_python(self, value):
        if self.ipv4_masked_network_re.search(value):
            # We were given a dotted-IP-style netmask
            # Validate it and transform into a CIDR mask
            ip, mask = value.split('/')
            mask = mask.split('.')

            # Convert the mask to an integer so we can "walk" its bits
            mask_int = (int(mask[0]) << 24) + (int(mask[1]) << 16) + (int(mask[2]) << 8) + int(mask[3])

            # The CIDR mask is the number of bits we count in the netmask
            cidr_mask = 0

            while mask_int > 0:
                # Modulo 2 gives us the current left-most bit
                bit = mask_int % 2
                # Now shift the whole number right
                mask_int = mask_int >> 1

                if bit == 1:
                    # Encountered a bit, add one to our mask
                    cidr_mask += 1
                elif cidr_mask > 0:
                    # We've already encountered at least one bit, means the mask isn't contiguous
                    raise ValidationError('Bad netmask ({mask})'.format(mask='.'.join(mask)))

            # Reassemble IP with CIDR mask
            value = '/'.join((ip, str(cidr_mask)))

        return value


class PirouteForm(forms.Form):
    """
    A consistent base form for Piroute

    Forms that extend this form will by default have all text, password, and
    date input widgets display placeholder text equal to their label. This can
    be overridden per form field by simply specifying a different placeholder
    attribute.

    Additionally, all form fields will automatically receive the 'form-control'
    CSS class (per Bootstrap requirements).
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update(
                        {
                            'class': field.widget.attrs.get('class', '') + ' form-control',
                        })
                if type(field.widget) in (forms.TextInput, forms.PasswordInput, forms.EmailInput, forms.DateInput, forms.NumberInput):
                    field.widget.attrs.update(
                            {
                                'placeholder': field.widget.attrs.get('placeholder', field.label or field_name),
                            })


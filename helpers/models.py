from django.db import models
from django.utils.translation import ugettext_lazy as _


from . import validators, forms


# Create your models here.

class IPNetworkField(models.Field):
    description = _("IP address or network")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        self.default_validators = [validators.validate_ipv4_network]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def get_internal_type(self):
        return 'CharField'

    def formfield(self, **kwargs):
        # Allow calling code to override our default form field
        defaults = {'form_class': forms.IPNetworkField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


from django.db import models


from . import validators


# Create your models here.

class IPNetworkField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        self.default_validators = [validators.validate_ipv4_network]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs


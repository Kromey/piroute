from django.db import models


# Create your models here.

class IPNetworkField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs


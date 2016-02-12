from django.db import models


from helpers.models import IPNetworkField


# Create your models here.
class Network(models.Model):
    POLICIES = (
            ('reject', 'Reject'),
            ('drop', 'Ignore'),
            ('accept', 'Accept'),
            )
    name = models.CharField(max_length=30)
    interface = models.CharField(max_length=10)
    ip_range = IPNetworkField()
    policy = models.CharField("default policy", choices=POLICIES, max_length=6)


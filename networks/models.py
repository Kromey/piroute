from django.db import models


from helpers import models as helpermodels


# Create your models here.
class Networks(models.Model):
    POLICIES = (
            ('reject', 'Reject'),
            ('drop', 'Ignore'),
            ('accept', 'Accept'),
            )
    name = models.CharField(max_length=30)
    interface = models.CharField(max_length=10)
    ip_range = helpermodels.IPNetworkField()
    policy = models.CharField("default policy", choices=POLICIES, max_length=6)


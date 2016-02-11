from django.db import models


# Create your models here.
class Networks(models.Model):
    POLICIES = (
            ('reject', 'Reject'),
            ('drop', 'Ignore'),
            ('accept', 'Accept'),
            )
    name = models.CharField(max_length=30)
    interface = models.CharField(max_length=10)
    ip_range = models.CharField(max_length=35)
    policy = models.CharField("default policy", choices=POLICIES)


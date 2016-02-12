from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


ipv4_network_re = r'^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}(/[0-2]?\d|/3[0-2])?\Z'
validate_ipv4_network = RegexValidator(ipv4_network_re, _('Enter a valid IPv4 network/address.'), 'invalid')


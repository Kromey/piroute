from django.test import TestCase
from django.core.exceptions import ValidationError


from . import forms


# Create your tests here.
class TestIPNetworkField(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.field = forms.IPNetworkField()

    def testSimpleAddress(self):
        self.assertEqual(self.field.clean('172.16.12.34'), '172.16.12.34')

    def testCIDRMask(self):
        self.assertEqual(self.field.clean('172.16.0.0/12'), '172.16.0.0/12')

    def testNetmask(self):
        # Netmasks get rewritten to CIDR masks
        self.assertEqual(self.field.clean('172.16.0.0/255.240.0.0'), '172.16.0.0/12')

    def testBadCIDRMask(self):
        self.assertRaisesMessage(ValidationError, 'Enter a valid IPv4 network/address.', self.field.clean, '172.16.0.0/36')

    def testBadNetmask(self):
        self.assertRaisesMessage(ValidationError, 'Bad netmask', self.field.clean, '172.16.0.0/255.138.0.0')
        self.assertRaisesMessage(ValidationError, 'Bad netmask', self.field.clean, '172.16.0.0/255.240.0.128')


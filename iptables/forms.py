from django import forms


from helpers.forms import PirouteForm


from . import formsets, services


class InterfacesForm(PirouteForm):
    internal_nic = forms.CharField()
    external_nic = forms.CharField()


class RuleForm(PirouteForm):
    action = forms.ChoiceField(choices=(('accept','Allow'),('drop','Ignore'),('reject','Block'),('forward','Redirect...')))
    enabled = forms.BooleanField(initial=True, required=False)
    nic = forms.ChoiceField(choices=(('int','Internal'),('ext','External')))
    service = forms.ChoiceField(choices=services.get_service_choices())
    proto = forms.ChoiceField(choices=services.PROTOCOL_LIST, required=False)
    port = forms.IntegerField(min_value=1, max_value=65535, required=False)
    comment = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        proto = cleaned_data.get('proto')
        port = cleaned_data.get('port')
        service = cleaned_data.get('service')

        if not (service or port):
            # No port/service provided, mark for deletion
            cleaned_data[forms.formsets.DELETION_FIELD_NAME] = True

        return cleaned_data

RuleFormset = formsets.selfcleanformset_factory(RuleForm, min_num=1, extra=0, can_order=True)


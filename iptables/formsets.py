from django import forms


class SelfCleanFormSet(forms.BaseFormSet):
    @property
    def cleaned_data(self):
        unclean_data = super().cleaned_data
        cleaned_data = [data for data in unclean_data
                        if data and not data.get('DELETE')]

        return cleaned_data

def selfcleanformset_factory(form, *args, **kwargs):
    return forms.formset_factory(form,
            formset=SelfCleanFormSet,
            can_delete=True,
            *args, **kwargs)


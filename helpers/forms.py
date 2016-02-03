from django import forms


class PirouteForm(forms.Form):
    """
    A consistent base form for Piroute

    Forms that extend this form will by default have all text, password, and
    date input widgets display placeholder text equal to their label. This can
    be overridden per form field by simply specifying a different placeholder
    attribute.

    Additionally, all form fields will automatically receive the 'form-control'
    CSS class (per Bootstrap requirements).
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update(
                        {
                            'class': field.widget.attrs.get('class', '') + ' form-control',
                        })
                if type(field.widget) in (forms.TextInput, forms.PasswordInput, forms.EmailInput, forms.DateInput, forms.NumberInput):
                    field.widget.attrs.update(
                            {
                                'placeholder': field.widget.attrs.get('placeholder', field.label or field_name),
                            })


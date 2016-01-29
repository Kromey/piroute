from django.shortcuts import render
from django.template.loader import render_to_string
from django.forms import formset_factory


from . import forms, utils

# Create your views here.

def index(request):
    rules = None

    if request.method == 'POST':
        ifaces = forms.InterfacesForm(request.POST)
        ruleformset = forms.RuleFormset(request.POST)
        if ifaces.is_valid() and ruleformset.is_valid():
            data = ruleformset.cleaned_data
            data.sort(key=lambda rule: rule['ORDER'] or 100000)
            rules = render_to_string('iptables/rules.v4', {'rules':utils.prep_rules(data)})
            ruleformset = forms.RuleFormset(initial=data)
    else:
        ifaces = forms.InterfacesForm()
        ruleformset = forms.RuleFormset()

    return render(request, 'iptables/index.html', {'ifaces':ifaces, 'ruleformset':ruleformset, 'rules':rules})

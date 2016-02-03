import os


from django.shortcuts import render


from . import utils


# Create your views here.

def index(request):
    load = os.getloadavg()

    context = {
            'load': load,
            'name': utils.get_system_detail(),
            'memory': utils.get_system_memory(),
            'disk': utils.get_disk_usage(),
            }

    return render(request, 'status/index.html', context)


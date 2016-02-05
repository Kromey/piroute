from django.shortcuts import render


from . import utils


# Create your views here.

def index(request):
    context = {
            'load': utils.get_system_load(),
            'name': utils.get_system_detail(),
            'memory': utils.get_system_memory(),
            'disks': utils.get_disk_usage(),
            }

    return render(request, 'status/index.html', context)


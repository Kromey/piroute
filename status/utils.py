import os


import psutil


def get_system_detail():
    uname = os.uname()

    name = "{node} ({sys} {release} {machine})".format(
            node=uname.nodename,
            sys=uname.sysname,
            release=uname.release,
            machine=uname.machine
            )

    return name


def get_system_memory():
    psmem = psutil.virtual_memory()

    mem = {
            'free': psmem.available,
            'total': psmem.total,
            'percent': round(psmem.available/psmem.total*100, 1),
            }
    return mem


def get_disk_usage():
    psdisk = psutil.disk_usage('/')

    disk = {
            'free': psdisk.free,
            'total': psdisk.total,
            'percent': round(psdisk.free/psdisk.total*100, 1),
            }
    return disk


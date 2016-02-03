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

    # What's "used" logically and what's "used" in the output don't really
    # mesh, so we calculate "used" as total less available.
    mem = {
            'total': psmem.total,
            'free': psmem.available,
            'used': psmem.total-psmem.available,
            'percentfree': round(psmem.available/psmem.total*100, 1),
            'percentused': round(100-psmem.available/psmem.total*100, 1),
            }
    return mem


def get_disk_usage():
    psdisk = psutil.disk_usage('/')

    disk = {
            'total': psdisk.total,
            'free': psdisk.free,
            'used': psdisk.used,
            'percentfree': round(psdisk.free/psdisk.total*100, 1),
            'percentused': round(psdisk.used/psdisk.total*100, 1),
            }
    return disk


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

    mem = "{free} free out of {total} total ({per:.1F}%)".format(
            free=sizeof_fmt(psmem.available),
            total=sizeof_fmt(psmem.total),
            per=psmem.available/psmem.total*100
            )
    return mem


def get_disk_usage():
    psdisk = psutil.disk_usage('/')

    disk = "{free} free out of {total} total ({per:.1F}%)".format(
            free=sizeof_fmt(psdisk.free),
            total=sizeof_fmt(psdisk.total),
            per=psdisk.free/psdisk.total*100
            )
    return disk


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "{size:.1F}{unit}{suffix}".format(
                    size=num,
                    unit=unit,
                    suffix=suffix
                    )
        num /= 1024.0
    return "{size:.1F}{unit}{suffix}".format(
            size=num,
            unit='Yi',
            suffix=suffix
            )


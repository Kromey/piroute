import os


import psutil


def get_system_load():
    osload = os.getloadavg()
    cpus = psutil.cpu_count()
    load = []

    for avg in osload:
        load.append(
                (
                    avg,
                    percent(avg/cpus),
                    ))

    return load


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
    psswap = psutil.swap_memory()

    # What's "used" logically and what's "used" in the output don't really
    # mesh, so we calculate "used" as total less available.
    mem = {
            'total': psmem.total,
            'free': psmem.available,
            'used': psmem.total-psmem.available,
            'buffers': psmem.buffers,
            'swaptotal': psswap.total,
            'swapfree': psswap.free,
            'swapused': psswap.used,
            'percentfree': percent(psmem.available/psmem.total),
            'percentused': percent(1-psmem.available/psmem.total),
            'percentbuffers': percent(psmem.buffers/psmem.total),
            'percentswapused': psswap.percent,
            }
    return mem


def get_disk_usage():
    disks = []

    for partition in psutil.disk_partitions():
        psdisk = psutil.disk_usage(partition.mountpoint)

        disks.append({
                'mountpoint': partition.mountpoint,
                'total': psdisk.total,
                'free': psdisk.free,
                'used': psdisk.used,
                'percentfree': percent(psdisk.free/psdisk.total),
                'percentused': percent(psdisk.used/psdisk.total),
                })
    return disks


def percent(val):
    return round(val*100, 1)


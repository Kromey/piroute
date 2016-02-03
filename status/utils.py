import os


def get_system_detail():
    uname = os.uname()

    name = "{node} ({sys} {release} {machine})".format(
            node=uname.nodename,
            sys=uname.sysname,
            release=uname.release,
            machine=uname.machine
            )

    return name


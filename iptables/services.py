
# Protocols
TCP = 'TCP'
UDP = 'UDP'
BOTH = 'Both'

PROTOCOL_LIST = (
        (TCP, TCP),
        (UDP, UDP),
        (BOTH, BOTH),
        )

# List of tuples defining services in the form (name, proto, port)
SERVICE_LIST = (
        ('SSH', TCP, 22),
        ('DNS', BOTH, 53),
        ('HTTP', TCP, 80),
        ('HTTPS', TCP, 443),
        )

# Separator between proto and port in service choices
SEPARATOR = '|'

def make_service_label(proto, port):
    return "{proto}{sep}{port}".format(
            proto=proto,
            sep=SEPARATOR,
            port=port,
            )


def get_service_choices():
    services = (
            (None,'Select...'),
            ('custom', 'Custom...'),
            )

    for service in SERVICE_LIST:
        services = services + ((service[0], service[0]),)

    return services


def get_proto_from_service_choice(service):
    proto, port = service.split(SEPARATOR)
    return proto


def get_port_from_service_choice(service):
    proto, port = service.split(SEPARATOR)
    return port


def decode_service(choice):
    for service in SERVICE_LIST:
        if choice == service[0]:
            return service[1], service[2]

    return None, None


def get_service_name(proto, port):
    for service in SERVICE_LIST:
        if proto == service[1] and port == service[2]:
            return service[0]

    return 'Custom'


def get_service(proto, port):
    label = make_service_label(proto, port)

    for service in get_service_choices():
        if label == service[0]:
            return label

    return None


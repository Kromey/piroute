from . import services


def prep_rules(rules):
    prepped = []

    for rule in rules:
        if rule['enabled']:
            prepped.append(prep_rule(rule))

    return prepped


def prep_rule(raw_rule):
    rule = dict(raw_rule)

    if rule['service'] != 'custom':
        proto, port = services.decode_service(rule['service'])

        if not (proto and port):
            raise ValueError("Unknown service: {service}".format(
                service=rule['service']
                ))

        rule['proto'] = proto
        rule['port'] = port

        if not rule['comment']:
            rule['comment'] = "{service} service ({proto}:{port})".format(
                    service=rule['service'],
                    proto=proto,
                    port=port
                    )

    return rule


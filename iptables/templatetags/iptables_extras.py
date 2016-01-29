from django import template
from django.template.loader import render_to_string


from .. import services


register = template.Library()


@register.simple_tag
def write_rule(rule):
    if rule['proto'] == services.BOTH:
        tcp_rule = dict(rule)
        tcp_rule['proto'] = services.TCP
        udp_rule = dict(rule)
        udp_rule['proto'] = services.UDP

        return "{tcp}{udp}".format(
                tcp=write_rule(tcp_rule),
                udp=write_rule(udp_rule))
    else:
        return render_to_string('iptables/write_rule.v4', {'rule':rule})


@register.simple_tag
def open_port(chain, proto, port, comment=None):
    if proto == 'both':
        return "{tcp}{udp}".format(
                tcp=open_port(chain, 'tcp', port, comment),
                udp=open_port(chain, 'udp', port, comment))
    else:
        if comment is None:
            comment = "Open {proto} port {port}".format(
                    proto=proto, port=port)

        context = {
                'chain': chain,
                'proto': proto,
                'port': port,
                'comment': comment,
                }
        return render_to_string('iptables/accept_rule.v4', context)


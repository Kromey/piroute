from django import template


register = template.Library()


@register.filter
def format_bytes(num):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "{size:.1F}{unit}B".format(
                    size=num,
                    unit=unit
                    )
        num /= 1024.0
    return "{size:.1F}{unit}B".format(
            size=num,
            unit='Yi'
            )


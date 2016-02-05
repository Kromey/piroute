from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def format_bytes(numbytes):
    val = numbytes

    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi','Yi']:
        if abs(val) < 2*1024.0:
            break
        val /= 1024.0

    if val >= 10.0:
        val = '{val:.0F}'.format(val=val)
    else:
        val = '{val:.1F}'.format(val=val)

    formatted = '<span title="{numbytes:,} Bytes">{size}&nbsp;{unit}B</span>'.format(
            numbytes=numbytes,
            size=val,
            unit=unit,
            )
    return mark_safe(formatted)


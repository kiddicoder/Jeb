from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter(name='custom_timesince')
def custom_timesince(value):
    delta = now() - value

    if delta.days < 1:
        seconds = delta.seconds
        minutes = seconds // 60
        hours = seconds // 3600

        if hours > 0:
            return f"{hours}h ago"
        elif minutes > 0:
            return f"{minutes}m ago"
        else:
            return f"{seconds}s ago"
    elif delta.days == 1:
        return "1d ago"
    elif delta.days < 7:
        return f"{delta.days}d ago"
    elif delta.days < 30:
        weeks = delta.days // 7
        return f"{weeks}w ago"
    elif delta.days < 365:
        months = delta.days // 30
        return f"{months}m ago"
    else:
        years = delta.days // 365
        return f"{years}y ago"

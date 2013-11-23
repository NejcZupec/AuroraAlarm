from django import template


register = template.Library()

@register.simple_tag
def progress_bar_interval(aurora_value):
    """
    This tag calculates new interval value.
    Input interval: 0...9
    Output interval: 0...100

    Keyword aruguments:
    aurora_value -- Current AuroraAlarm value
    """

    return int(100.0/9 * int(aurora_value))

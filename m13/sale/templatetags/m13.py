from django import template

register = template.Library()


def remove_m13(value):
    value = value.replace('M13', '')
    value = value.replace('Manufaktur13', '')
    return value

register.filter('remove_m13', remove_m13)


def max_15_chars(value):
    value = value.split()
    filter(None, value)
    if '-' in value:
        value.remove('-')
    return '-'.join(value)[:15]

register.filter('remove_m13', remove_m13)
register.filter('max_15_chars', max_15_chars)

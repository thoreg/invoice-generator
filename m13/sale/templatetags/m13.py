from django import template

register = template.Library()


def remove_m13(value):
    value = value.replace('M13', '')
    value = value.replace('Manufaktur13', '')
    return value

register.filter('remove_m13', remove_m13)

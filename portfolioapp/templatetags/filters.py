from django import template

register = template.Library()


@register.filter
def skill_level_to_percent(level):
    if level == 'Beginner':
        return 25
    elif level == 'Intermediate':
        return 50
    elif level == 'Advanced':
        return 75
    elif level == 'Expert':
        return 100
    return 0


@register.filter
def language_level_to_percent(level):
    if level == 'A1':
        return 14
    elif level == 'A2':
        return 28
    elif level == 'B1':
        return 42
    elif level == 'B2':
        return 56
    elif level == 'C1':
        return 70
    elif level == 'C2':
        return 84
    elif level == 'Native':
        return 100
    return 0

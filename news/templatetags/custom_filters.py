from django import template

register = template.Library()


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Должен быть текст!')
    nasty_list = [
        'редиска',
        'Редиска',
        'матрица',
        'Матрица',
        'цветы',
        'Цветы',
        'время',
        'Время',
        'место',
        'Место',
        'авто',
        'Авто',
    ]

    for item in nasty_list:
        if item in value:
            value = value.replace(item, f"{item[0]}{'*' * (len(item) - 1)}")
    return value

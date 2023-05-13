



def get_data_fig(*args, **kwargs):


    """Подвиг 5. Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
     На вход этой функции передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:

    type - булево значение True/False
    color - целое числовое значение
    closed - булево значение True/False
    width - целое значение

    Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в
    порядке их перечисления в тексте задания (если они были переданы).
     Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).

    Функцию выполнять не нужно, только определить."""


    p = sum(args)
    result = [p]
    if 'type' in kwargs:
        result.append(kwargs['type'])
    if 'color' in kwargs:
        result.append(kwargs['color'])
    if 'closed' in kwargs:
        result.append(kwargs['closed'])
    if 'width' in kwargs:
        result.append(kwargs['width'])

    return tuple(result)
print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))

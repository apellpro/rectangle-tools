def intersection(x1, y1, x2, y2, x3, y3, x4, y4) -> int:
    """Площадь пересечения прямоугольников"""
    width = min(x2, x4) - max(x1, x3)
    height = min(y1, y3) - max(y2, y4)
    if width < 0 or height < 0:
        return 0
    return width * height


def union(x1, y1, x2, y2, x3, y3, x4, y4) -> int:
    """Площадь объединения прямоугольников"""
    inter_area = intersection(**locals())
    first_area = abs(x1 - x2) * abs(y1 - y2)
    second_area = abs(x3 - x4) * abs(y3 - y4)
    return first_area + second_area - inter_area


def main():
    args = input('Введите 8 целых чисел (координаты): ')
    try:
        args = [int(i) for i in args.split()]
    except ValueError:
        print('Неверный формат ввода.')
        return
    if len(args) != 8:
        print('Введено неправильное количество аргументов.')
        return
    print(f'Площадь пересечения: {intersection(*args)}')
    print(f'Площадь объединения: {0}')

def intersection(x1, y1, x2, y2, x3, y3, x4, y4) -> int:
    """Площадь пересечения прямоугольников"""
    width, height = 0, 0
    if x1 <= x3 <= x2:
        width = x2 - x3
    if x3 <= x1 <= x4:
        width = x4 - x1
    if y1 >= y3 >= y2:
        height = y3 - y2
    if y3 >= y1 >= y4:
        height = y1 - y4
    return abs(width * height)


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
    print(f'Площадь пересечения: {0}')
    print(f'Площадь объединения: {0}')

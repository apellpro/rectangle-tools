from .functions import intersection, union


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
    print(f'Площадь объединения: {union(*args)}')


if __name__ == '__main__':
    main()

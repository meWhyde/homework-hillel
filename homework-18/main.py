def cache_decorator(func):
    def check(*args, **kwargs):
        check_key = args + tuple(kwargs.items())
        if check_key not in check_cache:
            check_cache[check_key] = func(*args, **kwargs)
        return check_cache[check_key]

    check_cache = dict()
    return check


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    """
    Функция считает площадь треугольника
    :param a: Сторона треугольника
    :param b: Сторона треугольника
    :return: Площадь
    """

    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    """
    Функция считает площадь круга
    :param r: Радиус
    :return: Площадь
    """

    print(f'Вызвана функция circle_area с аргументом {r}')
    return 3.14 * (r * r)


print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))  # Тело функции не выполниться так как функция ранее вызывалась с такими аргументами
print('Результат выполнения circle_area(20):', circle_area(20))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
print('Результат выполнения triangle_area(10, 10):', triangle_area(10, 10))  # Тело функции выполниться так как функция вызывается в первый раз с такими аргументами
print('Результат выполнения circle_area(20):', circle_area(20))  # Тело функции не выполниться так как функция ранее вызывалась с такими аргументамиa(20):', circle_area(20))  # Тело функции не выполниться так как функция ранее вызывалась с такими аргументами
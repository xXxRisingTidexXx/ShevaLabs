"""
Лабораторна робота №2
ІПЗ - 12, Петраківський Данило
"""


def divide_integers():
    """
    #1
    """
    name = input('Ваше ім\'я: ')
    x = int(input('Введіть X: '))
    y = int(input('Введіть Y: '))
    print('{} поділив {} на {}, отримавши {} цілих і {} в залишку, або {:f}'.format(name, x, y, x // y, x % y, x / y))


def sum_digits():
    """
    #2
    """
    numb = input('Введіть число: ')
    print('Сума цифр числа {0} складає {1}. 1 <= {1} <= 27'.format(numb, int(numb[0]) + int(numb[1]) + int(numb[2])))


def calculate_last_digit():
    """
    #3
    """
    numb = int(input('Введіть число: '))
    print('Остання цифра: {}'.format(numb % 10))


def convert_bits():
    """
    #4
    """
    total_bits = int(input('Число біт: '))
    total_bytes = total_bits // 8
    b = total_bytes % 1024
    total_bytes //= 1024
    kb = total_bytes % 1024
    total_bytes //= 1024
    mb = total_bytes % 1024
    print('{} Мбайт, {} Кбайт, {} байт, {} біт'.format(mb, kb, b, total_bits % 8))


def convert_seconds():
    """
    #5
    """
    seconds = int(input('Число секунд: '))
    print('{} хв. {} сек. '.format(seconds // 60, seconds % 60))


def determinate_time():
    """
    #6
    """
    minutes = int(input('Число хвилин: ')) % 1440
    print('{}:{}'.format(extend(minutes // 60), extend(minutes % 60)))


def extend(n):
    return str(n) if n >= 10 else '0{}'.format(n)


def calc_difference():
    """
    #7
    """
    h1 = int(input('Введіть h1: '))
    m1 = int(input('Введіть m1: '))
    s1 = int(input('Введіть s1: '))
    h2 = int(input('Введіть h2: '))
    m2 = int(input('Введіть m2: '))
    s2 = int(input('Введіть s2: '))
    print('{} сек.'.format((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1))

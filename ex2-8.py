# Задание 2.8
# Нужно получить: ValueError: math domain error
# Причина: у отрицательного числа нет вещественного квадратного корня.
# Так же ведёт себя math.log(-1), math.acos(2), math.asin(5).

import math

print(math.sqrt(-1))

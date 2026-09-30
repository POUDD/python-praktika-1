# Задание 2.9
# Нужно получить: OverflowError: math range error
# Причина: ответ функции не помещается в float.
# Максимум float примерно 1.8e+308, а e**1000 это примерно 10**434.

import math

print(math.exp(1000))

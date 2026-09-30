# Задание 1.7
# Что за странное выражение и почему результат -2?
#
# (True * 2 + False) * -True

# В Python True и False это числа 1 и 0.
# Тип bool в Python является подтипом int, поэтому с True и False
# можно делать обычную арифметику.

print("True == 1:", True == 1)
print("False == 0:", False == 0)
print("откуда это видно:", bool.__mro__)
print()

# Считаем по шагам:
print("True * 2 =", True * 2)
print("True * 2 + False =", True * 2 + False)
print("-True =", -True)
print("(True * 2 + False) * -True =", (True * 2 + False) * -True)
print()

# Результат арифметики получается обычное целое число, а не True/False.
ответ = (True * 2 + False) * -True
print("тип ответа:", type(ответ).__name__, "значение:", ответ)
print()

# Ещё примеры, чтобы было понятнее:
print("True + True =", True + True)
print("True - True =", True - True)
print("sum([True, False, True]) =", sum([True, False, True]))
print()

# Вывод: True это 1, False это 0, поэтому (2 + 0) * (-1) = -2.

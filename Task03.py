# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from multiprocessing.dummy import Value


n = int(input("Введите число: "))
V = {n: round((1 + (1 / n)) ** n) for n in range(1, n + 1)}
print(V)
print(sum(V.values()))
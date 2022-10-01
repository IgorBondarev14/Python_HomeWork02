# Реализуйте алгоритм перемешивания списка

N = int(input("Введите размер списка (целое число): "))
while N < 1:
    N = int(input("Введите размер списка (целое число): "))
from random import randint, shuffle
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)
import random
random.shuffle(numbers)
print(numbers)
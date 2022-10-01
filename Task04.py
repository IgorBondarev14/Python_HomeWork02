# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной
# строке одно число.

N = int(input("Введите размер списка (целое число): "))
while N < 1:
    N = int(input("Введите размер списка (целое число): "))
from random import randint
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)

quantity = int(input("Введите количествол элементов для умножения: "))
while quantity > N or quantity < 0:
    print("Число элементов для умножения не может превышать размер списка.")
    quantity = int(input("Введите количествол элементов для умножения: "))
if quantity == 0:
    print("Элементы для умножения не выбраны")
else:
    composition = 1
    for i in range(quantity):
        index = int(input("Введите индекс элемента для умножения: "))
        while index < 0 or index > N:
            print("Индекс должен находиться в пределах от 0 до " + N)
            index = int(input("Введите индекс элемента для умножения: "))
        composition = composition * numbers[index]
    print("Произведение элементов на указанных позициях равно: " + str(composition))

data = open('file.txt', 'w')
for i in range(N):
    data.write(str(numbers[i]))
    data.write("\n")  
data.close()
exit()
import random
from random import randint

matrix = []
n = int(input("Введите количество строк(рядов):"))
m = int(input("Введите количество столбцов(мест):"))
kol = int(input("Введите количество людей в группе"))
for i in range(n):
    strk = [randint(0,1) for j in range(m)]
    matrix.append(strk)


for k in range(n):
    print(*matrix[k])
result = 0
for ryad in range(n):
    svobod_mesta = 0
    for seat in matrix[ryad]:
        if seat == 0:
            svobod_mesta += 1  # Увеличиваем счетчик, если место свободно
            if svobod_mesta == kol:
                result = ryad + 1  # Номер ряда (с 1)
                break
        else:
            free_streak = 0  # Сбрасываем счетчик при встрече с занятым местом
    if result > 0:
        break  # Прерываем цикл, если нашли подходящий ряд


if result > 0:
    print(f"Группа может сесть в ряду номер {result}.")
else:
    print("Нет подходящего ряда.")





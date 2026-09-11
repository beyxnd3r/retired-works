a = []
while 1:
    b = input("Введите число(Для остановки нажмите enter)")
    if b == "":
        break
    try:
        a.append(int(b))
    except ValueError:
        print("Пожалуйста, введите корректное число.")

avg = sum(a)/len(a)

less = []
more = []

for number in a:
        if number < avg:
            less.append(number)
        elif number > avg:
            more.append(number)

print("Среднее значение списка", avg)
print(*less)
print(*more)

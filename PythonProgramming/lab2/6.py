import random
secret = random.randint(1, 10)
a = 0
print("Хорошо, я загадал число. Попробуй его отгадать")
c = 0
while 1:
    a+= 1
    num = int(input("Введите число"))
    print("Попыток", a)


    if num < secret:
        print("Ты близок число больше")
    elif num > secret:
        print("Число меньше")

    if num == secret:
        print("Поздравляю! Вы угадали!, Попыток: ", a)
        q = int(input("Хотите попробовать еще раз? 1 если да, 2 если нет"))
        if q == 1:
            continue
        else:
            break

    else:
        print("Нее, ты не угадал. Попробуй снова")

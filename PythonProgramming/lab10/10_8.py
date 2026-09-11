n = int(input("Введите число"))
m = int(input("Введите второе число"))
if n < 3 or n > 50 or m < 3 or m > 50:
    print("Неправильный диапазон")
else:
    for i in range(n):
        if i % 2 == 0:
            print(m * "#")
        else:
            if (i // 2) % 2 == 0:
                print("." * (m - 1) + "#")
            else:
                print("#" + "." * (m - 1))
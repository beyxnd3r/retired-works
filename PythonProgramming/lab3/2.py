a = input("Введите словосочетание ").split()
if len(a) < 2 or len(a) > 2:
    print("Некорректно")
else:
    a.reverse()
    print(a[0], a[1])




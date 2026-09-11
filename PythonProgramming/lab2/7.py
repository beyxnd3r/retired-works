b = input("Введите шестизначное число ")
if int(b[0])+int(b[1])+int(b[2]) == int(b[3])+int(b[4])+int(b[5]):
    print("Поздравляем ваш билет счастливый!")
elif int(b[0])+int(b[1])+int(b[2]) != int(b[3])+int(b[4])+int(b[5]):
    print("Обычный билет")
else:
    print("Некорректное число")
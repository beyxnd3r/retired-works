a = input('Введите слово')
for i in range(len(a)):
    if i<len(a)-1:
        print(a[i]+ '.' , end='')
    else:
        print(a[i], end='')


with open(r'C:\file7.txt', 'r', encoding='utf-8') as file:
    female_names = []
    for line in file:
        parts = line.split()
        if parts:
            female_names.append(parts[0])

with open(r'C:\file8.txt', 'r', encoding='utf-8') as file:
    male_names = []
    for line in file:
        parts = line.split()
        if parts:
            male_names.append(parts[0])

try:

    n = int(input("Введите количество имен: "))
    gender = input("Введите пол (м - мужские, ж - женские): ").strip().lower()


    if gender == 'м':
        selected_names = male_names[:n]
    elif gender == 'ж':
        selected_names = female_names[:n]
    else:
        print("Некорректный ввод пола. Введите 'м' или 'ж'.")
        selected_names = []


    if selected_names:
        for name in selected_names:
            print(name)
    else:
        print("Нет данных для вывода.")

except ValueError:
    print("Ошибка ввода! Убедитесь, что количество имен - это число.")

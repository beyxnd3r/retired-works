# Ввод размеров матрицы
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

# Создание пустой матрицы
matrix = [[0] * m for s in range(n)]

# Заполнение матрицы
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:  # Первый ряд или первый столбец
            matrix[i][j] = 1
        else:
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

# Вывод матрицы
print("Сформированная матрица:")
for row in matrix:
    print(" ".join(f"{elem:6}" for elem in row))

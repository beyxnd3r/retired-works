
n, m = map(int, input("Введите размер матрицы").split())


matrix = [list(map(int, input("Введите матрицу(В соответситвии с размером)").split())) for k in range(n)]

transposed = [[matrix[j][i] for j in range(n)] for i in range(m)]

for row in transposed:
    print(*row)

rs = []
r = 1
while r != 0 :

    r = int(input("Введите рост человека (или 0 для завершения): "))

    if r == 0:
        break
    elif r < 0:
        print("Отрицательный рост не учитывается.")
    else:
        rs += [r]

if len(rs) < 2:
    print("Некого сравнивать")
else:
    maxrs = max(rs)
    minrs = min(rs)
    print(f"Самый высокий человек с ростом:", maxrs)
    print(f"Самый низкий человек с ростом:", minrs )
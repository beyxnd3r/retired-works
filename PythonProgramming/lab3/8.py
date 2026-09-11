a =  input("Введите счет матча(Формат: Команда-Команда A:B")
a1 = a.split()
k = a1[0].split('-')
s = a1[1].split(':')
score_team_1 = int(s[0])
score_team_2 = int(s[1])
if score_team_1 > score_team_2:
    print(k[0])
elif score_team_1 < score_team_2:
    print(k[1])
else:
    print("Ничья")

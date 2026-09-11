a = input("Введите номер карты")
digits = [int(d) for d in a]
chet_sum = sum(digits[-1::-2])
nechet_sum = 0
for d in digits[-2::-2]:
    doubled = d * 2
    if doubled > 9:
        doubled -= 9
    nechet_sum += doubled
total_sum = chet_sum + nechet_sum
if total_sum % 10 == 0:
    print(f"{a} - Корректный номер")
else:
    print(f"{a} - Некорректный номер")


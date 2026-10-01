# 5.py: Naive Haiku check
a = input("Введите текст Хайку")
asp = a.split()
if len(asp)<3:
    print("Не Хайку")
else:
    print("Хайку")

with open(r'C:\file5.txt', encoding='utf-8') as file:
    acad = file.read()
    if "Academy" in acad:
        print("В 5 файле есть слово academy")
        file.close()
    else:
        file.close()
with open(r'C:\file6.txt', encoding='utf-8') as file:
    acad = file.read()
    if "Academy" in acad:
        print("В 6 файле есть слово academy")
        file.close()
    else:
        file.close()

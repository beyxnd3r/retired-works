
with open(r'C:\file5z.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()
    middle_index = len(text) // 2
    text.insert(middle_index, "Ой, а что я делаю в середине этого файла\n")
with open(r'C:\file5z.txt', 'w', encoding='utf-8') as file:
    file.writelines(text)

print("Строка успешно добавлена в середину файла.")
# 10_6.py: Reverse each line of a file

with open(r'C:\file6z.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

with open(r'C:\file6z.txt', 'w', encoding='utf-8') as file:
    for i in text:
        file.write(i[::-1])

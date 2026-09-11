import random

a = int(input("Создаем пароль. Введите длину"))
b = input("Нужны ли заглавные буквы?")
c = input("Нужны ли строчные буквы?")
d = input("Нужны ли цифры?")
e = input("Нужны ли специальные символы?")
passwd = " "
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
characters = ''
if b == "Да" or b == "да":
    characters += uppercase_letters
if c == "Да" or c == "да":
    characters += lowercase_letters
if d == "Да" or d == "да":
    characters += digits
if e == "Да" or e == "да":
    characters += special_characters

for i in range(a):
    passwd += random.choice(characters)
print("Ваш пароль", passwd)
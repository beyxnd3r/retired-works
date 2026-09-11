a = input("Введите 1 слово которое нужно заменить")
b = input("Введите 2 слово которое нужно заменить")
c = input("Введите 3 слово которое нужно заменить")

for word in [a, b, c]:
    if len(word) < 10:
        print(word)
    else:
        abbreviated_word = f"{word[0]}{len(word) - 2}{word[-1]}"
        print(abbreviated_word)


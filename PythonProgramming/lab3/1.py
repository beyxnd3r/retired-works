a = input("Введите предложение: ")

b = a.split()

result = ""

previous_word = ""

for i in b:

    if i != previous_word:

        if result:
            result += " "
        result += i

    previous_word = i

print("Предложение без подряд идущих повторяющихся слов:", result)

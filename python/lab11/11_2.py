points = {
    '1': ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    '2': ['D', 'G'],
    '3': ['B', 'C', 'M', 'P'],
    '4': ['F', 'H', 'V', 'W', 'Y'],
    '5': ['K'],
    '8': ['J', 'X'],
    '10': ['Q', 'Z']
}

word = input("Введите слово:")
word = word.upper()
total_points = 0

for letter in word:
    for key, value in points.items():
        if letter in value:
            total_points += int(key)

print(f"Общее количество очков за слово: {total_points}")

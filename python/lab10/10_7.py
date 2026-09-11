import random
with open(r'C:\file7z.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    word = text.split()
    p = ''
    p = random.choice(word)+random.choice(word)
    while len(p)<8 or len(p)>10:
        p = random.choice(word)+random.choice(word)
print(p)

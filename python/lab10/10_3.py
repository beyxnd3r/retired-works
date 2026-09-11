counte = 0
count = 0
letter = "e"
with open(r'C:\file6.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    countsplt = text.split()
    count = len(countsplt)
    for word in countsplt:
        if letter in word.lower():
            counte += 1

percantage = counte/count*100



print(count)
print(counte)
print(f"{percantage:.2f} %")
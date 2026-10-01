# 5.py: Find place in height-sorted line
a = int(input("Рост Андрея"))
b = [215,207,196,176,168,166]
start = 1
for i in b:
    if i > a:
        start += 1
    elif i==a:
        start+=1
print(start)
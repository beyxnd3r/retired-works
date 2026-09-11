import random

a = ["Q","A"]
n = int(input())
count = 0
count1 = 0
s = ""
for i in range(n):
    r = (random.choice(a))
    s += r
    print(r, end='')
print("")
for letter in s:
    if letter == "Q":
        count += 1
for letter1 in s:
    if letter1 == "A":
        count1+=1
if count == count1:
    print("+")
if count != count1:
    print("-")

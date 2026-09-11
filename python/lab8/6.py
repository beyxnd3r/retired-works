import random
a = ["O","P"]
count = 0
total = 0
last = None

while count<3:
    b = random.choice(a)
    total +=1
    print(b, end= ' ')

    if b == last:
        count +=1
    else:
        count = 1
    last = b

print("Попыток:",total )
dv = "10110"

d = 0
s = 0

for i in range(len(dv) -1, -1, -1):
    if dv[i] == '1':
        d += 2**s
    s+=1
print(d)
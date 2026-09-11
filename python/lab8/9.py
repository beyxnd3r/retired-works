a = [1,10]
d = [0,10]
c = [10,10]
ub = 0
b = 0
one = False
two = False
three = False
print("Комнаты в общежитии")
print(*a)
print(*d)
print(*c)
if a[0]==a[1]:
    print("В первом занято")
    one = True
else:
    print("Есть места в первой общаге")
    ub = ub+1

if d[0]==d[1]:
    print("Во второй занято")
    two = True
else:
    print("Во второй свободно")
    ub=ub+1
if c[0]==c[1]:
    print("В третьей занято")
    three = True
else:
    print("Го в третью")
    ub = ub+1
if one == True and two == True and three == True:
    print("0")
print(ub)

a = [1,"a",3,4,"b",6]
b = [a[0],a[2],a[3],a[5]]
c = [a[1], a[4]]
del(a)
print(*b)
print(*c)

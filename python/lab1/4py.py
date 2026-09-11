a1 = int(input("Input first side of the triangle"))
a2 = int(input("Input second side of the triangle"))
a3 = int(input("Input third side of the triabgle"))

if a1==a2==a3:
    print("Sides are the same")
elif a1==a2 or a1==a3:
    print("Two sides are the same")
else:
    print("Sides are different broski")
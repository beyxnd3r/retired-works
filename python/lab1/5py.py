m = input("Input name of the month")

if m in ["December","January","March","May","July","August","October"]:
    print("Your month has 31 days")
elif m in["April","June","September","November"]:
    print("Your month has 30 days")
elif m=="February":
    print("28 or 29 days bruh")
else:
    print("Input error")
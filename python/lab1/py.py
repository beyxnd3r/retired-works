# py.py - A program that takes in the number of days, hours, minutes and seconds and converts it into seconds.
a = (int(input("Input days ")))
b = (int(input("Input hours ")))
c = (int(input("Input minutes ")))
d = (int(input("Input seconds ")))
sec =((d*86400)+(b*3600)+(c*60)+d)
print(sec)

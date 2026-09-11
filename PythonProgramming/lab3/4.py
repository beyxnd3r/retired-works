a = input("Введите отзыв")

if "Не плохо" in a or "не плохо" in a:
    a = a.replace("Не плохо", "Хорошо")
    a = a.replace("не плохо", "хорошо")
    print(a)
elif "Не плохая" in a or "не плохая" in a:
    a = a.replace("Не плохая", "Хорошая")
    a = a.replace("не плохая", "хорошая")
    print(a)
elif "Не плохой" in a or "не плохой" in a:
    a = a.replace("Не плохой", "Хороший")
    a = a.replace("не плохой", "хороший")
    print(a)
else:
    print(a)





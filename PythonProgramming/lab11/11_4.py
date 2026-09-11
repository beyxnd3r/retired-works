from random import randint
import PySimpleGUI as sg

sg.theme("DarkBrown")

layout = [
    [sg.Image(r"C:\Users\glebg\Downloads\a3e63fd24b585ada2bdb845eee45d982.png")],
    [sg.Text("Границы рандома:", font="20px"),
     sg.InputText(font="20px", size=(15, None), key="min_val"),
     sg.Text(":", font="20px"),
     sg.InputText(font="20px", size=(15, None), key="max_val")],
    [sg.Button("Сгенерировать", button_color="green", font="70px", size=(70, 2))],
    [sg.Input(key="res", font="70px", size=(70, 2), readonly=True)]
]

window = sg.Window("РНГ", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Сгенерировать":
        try:

            min_val = int(values["min_val"])
            max_val = int(values["max_val"])


            if min_val > max_val:
                sg.popup_error("Минимальное значение не может быть больше максимального!")
                continue


            random_number = randint(min_val, max_val)


            window["res"].update(random_number)
        except ValueError:
            sg.popup_error("Пожалуйста, введите корректные числовые границы!")

window.close()

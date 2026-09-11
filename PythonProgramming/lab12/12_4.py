from random import randint
import PySimpleGUI as sg


def to_signed_binary(number, bits=8):
    """Функция для преобразования числа в двоичное представление в прямом, обратном и дополнительном кодах."""
    if number >= 0:
        # Прямой код для положительных чисел и нуля
        real = bin(number)[2:].zfill(bits)
        rev = real  # Обратный код для положительных чисел совпадает с прямым
        dlc = real  # Дополнительный код для положительных чисел совпадает с прямым
    else:
        # Прямой код для отрицательных чисел
        real = bin((1 << bits) + number)[2:].zfill(bits)

        # Обратный код для отрицательных чисел (инвертируем все биты прямого кода)
        rev = ''.join('1' if bit == '0' else '0' for bit in real)

        # Дополнительный код для отрицательных чисел (прибавляем 1 к обратному коду)
        dlc = bin(int(rev, 2) + 1)[2:].zfill(bits)

    return real, rev, dlc

sg.theme("Default")

layout = [
    #[sg.Image(r"C:\Users\glebg\Downloads\a3e63fd24b585ada2bdb845eee45d982.png")],
    [sg.Text("Число:", font="20px"),
     sg.InputText(font="20px", size=(103,None), key="number1"),],
    [sg.Button("Узнать значения", button_color="green", font="70px", size=(110, 2))],
    [sg.Text("Прямой код:", font="20px"), sg.InputText(key="real1", font="70px", size=(25, 2)),
     sg.Text(":", font="20px"),sg.Text("Обр. код", font="20px"),sg.InputText(font="20px", size=(25, None), key="rev1"),
     sg.Text(":", font="20px"),sg.Text("Доп. код", font="20px"),sg.InputText(font="20px", size=(25, None), key="dlc1")]
]

window = sg.Window("Значения ", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Узнать значения":
        try:
            number = int(values["number1"])

            if -128 <= number <= 127:
                real,rev,dlc = to_signed_binary(number)

                window["real1"].update(real)
                window["rev1"].update(rev)
                window["dlc1"].update(dlc)
            else:
                sg.popup_error("Не в диапозоне")
        except ValueError:
            sg.popup_error("Не то число")



window.close()

import PySimpleGUI as sg
from random import randint

c_image = [[sg.Image("./bio.png")]]
c_input = [[sg.Text("Введите число [-127;128]:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="number", enable_events=True)],
           [sg.Text("Прямой:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="res")],
           [sg.Text("Обратный:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="res_inverse")],
           [sg.Text("Дополнительный:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="res_compliment")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бинарных чисел", layout)

def simulate_bacteria(micro, k, count):
    b = randint(0, 4)
    if count > 1:
        return simulate_bacteria((micro*k + b), k, count - 1)
    else:
        return (micro*k + b)

while True:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    # Input validation
    if value["number"] and event == "number":
        try:
            number = int(value["number"]) 
            
            if number > 128 or number < -127:
                window["number"].update(value["number"][:-1])
        except:
            if len(value["number"]) == 1 and value["number"][0] == "-":
                continue
            window["number"].update(value["number"][:-1])

    if value["number"] and event == "Рассчитать":
        number = number & ((1 << 8) - 1)
        inv_number = ~number & ((1 << 8) - 1)
        
        window["res"].update(f"{number:08b}")
        window["res_inverse"].update(f"{inv_number:08b}")
        window["res_compliment"].update(f"{inv_number + 1:08b}")

window.close()


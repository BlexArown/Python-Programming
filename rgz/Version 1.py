import PySimpleGUI as sg
import random
from time import sleep

# Change theme to something lighter and pleasant
sg.theme('LightBlue')

# Constants for moves
ROCK = 1
PAPER = 2
SCISSORS = 3

def validate_input(count, name):
    """Validate user input for count and name."""
    if not count.isdigit() or len(name) < 1 or int(count) <= 0:
        return False
    return True

a = 0
b = 0
sum = 0

image1 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\камень.png"
image2 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\бумага.png"
image3 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\ножницы.png"
image4 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\start.png"
image5 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\choose.png"
image6 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\win.png"
image7 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\lose.png"
image8 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\non.png"

c_input = [[sg.Image(r"C:\Users\Саша\Documents\Python Вуз\rgz\images\hands.png")],
           [sg.Text("Введите своё имя > ", font="Arial 20"), sg.Input(font="Arial 20", size=(20, 0), key="name")],
           [sg.Text("Введите количество раундов > ", font="Arial 20"),
            sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Button("Играть", font="Arial 20")]]
c_image = [[sg.Button(image_filename=image1, key='-BUTTON1-', border_width=0)],
           [sg.Button(image_filename=image2, key='-BUTTON2-', border_width=0)],
           [sg.Button(image_filename=image3, key='-BUTTON3-', border_width=0)]]
c_comp = [[sg.Text(key="text", font="Arial 26")],
          [sg.Text('  Компьютер   ', font="Arial 20")],
          [sg.Image(filename=image5, key='COMP')],
          [sg.Text('       Вы  ', font="Arial 20")],
          [sg.Image(key='-IMAGE-')]]
a_image = [[sg.Image(r"C:\Users\Саша\Documents\Python Вуз\rgz\images\win.png")],
           [sg.Button("Закрыть")]]
b_image = [[sg.Image(r"C:\Users\Саша\Documents\Python Вуз\rgz\images\lose.png")],
           [sg.Button("Закрыть")]]
n_image = [[sg.Image(r"C:\Users\Саша\Documents\Python Вуз\rgz\images\non.png")],
           [sg.Button("Закрыть")]]

layout = [
    (sg.Column(c_input, justification='right'),)
]

game = [
    (sg.Column(c_image), sg.VSeperator(), sg.Column(c_comp, justification='right'))
]

window = sg.Window("Меню", layout)

while True:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    count = value['count']
    name = value['name']

    if validate_input(count, name):
        print(name)
        print(count)
        namm = name
        conr = int(count)
        window.close()
        break
    else:
        sg.popup("Введите корректные данные")

window = sg.Window("Камень-Ножницы-Бумага", game)

while True:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    print("read")

    if event == '-BUTTON1-':
        new = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\камень.png"
        window['-IMAGE-'].update(new)
        con = ROCK
    if event == '-BUTTON2-':
        new = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\бумага.png"
        window['-IMAGE-'].update(new)
        con = PAPER
    if event == '-BUTTON3-':
        new = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\ножницы.png"
        window['-IMAGE-'].update(new)
        con = SCISSORS

    if event in ['-BUTTON1-', '-BUTTON2-', '-BUTTON3-']:
        ran = random.randint(ROCK, SCISSORS)
        print("Рандом равен >", ran)
        if ran == ROCK:
            new = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\камень.png"
            window['COMP'].update(new)
            print("rock")
        elif ran == PAPER:
            new = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\бумага.png"
            window['COMP'].update(new)
            print("paper")
        elif ran == SCISSORS:
            new = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\ножницы.png"
            window['COMP'].update(new)
            print("nife")
        conr -= 1
        if (con == ROCK and ran == PAPER or con == PAPER and ran == SCISSORS or con == SCISSORS and ran == ROCK):
            b += 1
        elif (con == ROCK and ran == SCISSORS or con == PAPER and ran == ROCK or con == SCISSORS and ran == PAPER):
            a += 1
        elif con == ran:
            a += 1
            b += 1
        resau = f'Комп {b} - {namm} {a}'
        window['text'].update(resau)
        if conr == 0:
            break

print(a)
print(b)
if a > b:
    window = sg.Window("Победа", a_image)
    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, "Закрыть"):
            break
elif b > a:
    window = sg.Window("Поражение", b_image)
    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, "Закрыть"):
            break
else:
    window = sg.Window("Ничья", n_image)
    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, "Закрыть"):
            break
lin = namm, "Счёт", a, "-", b
line = str(lin)
print(line)
with open(r'C:\Users\Egor\Desktop\RGZ\RGZ.txt', 'a', encoding='utf-8') as file:
    file.writelines(line + "\n")




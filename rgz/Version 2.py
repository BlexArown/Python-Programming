import PySimpleGUI as sg
import random
from time import sleep
import os

sg.theme('DarkGreen')

ROCK = 1
PAPER = 2
SCISSORS = 3

FILE_PATH = r"C:\Users\Саша\Documents\Python Вуз\rgz\Запись.txt"

def validate_input(count, name):
    if not count.isdigit() or len(name) < 1 or int(count) <= 0:
        return False
    return True

def view_matches():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            matches = file.read()
    else:
        matches = "Нет записанных матчей."
    layout = [
        [sg.Multiline(matches, size=(50, 20), disabled=True, font="Arial 12")],
        [sg.Button("Закрыть")]
    ]
    window = sg.Window("Записанные матчи", layout)
    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Закрыть"):
            break
    window.close()

def reset_matches():
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        file.write("")
    sg.popup("Записи матчей сброшены.")

def play_game():
    global total_games, total_a, total_b

    a = 0
    b = 0

    image1 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\камень.png"
    image2 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\бумага.png"
    image3 = r"C:\Users\Саша\Documents\Python Вуз\rgz\images\ножницы.png"
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
    a_image = [[sg.Image(image6)],
               [sg.Button("Закрыть")]]
    b_image = [[sg.Image(image7)],
               [sg.Button("Закрыть")]]
    n_image = [[sg.Image(image8)],
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
            return

        count = value['count']
        name = value['name']

        if validate_input(count, name):
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
            return

        if event == '-BUTTON1-':
            new = image1
            window['-IMAGE-'].update(new)
            con = ROCK
        if event == '-BUTTON2-':
            new = image2
            window['-IMAGE-'].update(new)
            con = PAPER
        if event == '-BUTTON3-':
            new = image3
            window['-IMAGE-'].update(new)
            con = SCISSORS

        if event in ['-BUTTON1-', '-BUTTON2-', '-BUTTON3-']:
            ran = random.randint(ROCK, SCISSORS)
            if ran == ROCK:
                new = image1
                window['COMP'].update(new)
            elif ran == PAPER:
                new = image2
                window['COMP'].update(new)
            elif ran == SCISSORS:
                new = image3
                window['COMP'].update(new)

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

    if a > b:
        window = sg.Window("Победа", a_image)
    elif b > a:
        window = sg.Window("Поражение", b_image)
    else:
        window = sg.Window("Ничья", n_image)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Закрыть"):
            break

    lin = namm, "Счёт", a, "-", b
    line = str(lin)
    with open(FILE_PATH, 'a', encoding='utf-8') as file:
        file.writelines(line + "\n")

    total_games += 1
    total_a += a
    total_b += b

if __name__ == "__main__":
    total_games = 0
    total_a = 0
    total_b = 0

    layout = [
        [sg.Text("Камень-Ножницы-Бумага", font="Arial 26")],
        [sg.Button("Играть", size=(20, 2), font="Arial 16")],
        [sg.Button("Просмотр матчей", size=(20, 2), font="Arial 16")],
        [sg.Button("Сбросить записи матчей", size=(20, 2), font="Arial 16")],
        [sg.Button("Выход", size=(20, 2), font="Arial 16")]
    ]

    main_window = sg.Window("Главное меню", layout)

    while True:
        event, _ = main_window.read()
        if event == sg.WIN_CLOSED or event == "Выход":
            break
        if event == "Играть":
            play_game()
        if event == "Просмотр матчей":
            view_matches()
        if event == "Сбросить записи матчей":
            reset_matches()

    main_window.close()


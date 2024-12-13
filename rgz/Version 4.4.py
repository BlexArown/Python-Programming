import PySimpleGUI as sg
import random
from time import sleep
import os

# Change theme to something lighter and pleasant
sg.theme('LightBlue')

# Constants for moves
ROCK = 1
PAPER = 2
SCISSORS = 3

FILE_PATH = r"C:\Users\Саша\Documents\Python Вуз\rgz\Запись.txt"

def validate_input(count, name):
    """Validate user input for count and name."""
    if not count.isdigit() or len(name) < 1 or int(count) <= 0:
        return False
    return True

def view_matches():
    """Display recorded matches."""
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
    """Reset the match records."""
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

def play_tic_tac_toe():
    """Start the Tic-Tac-Toe game."""
    board = [["" for _ in range(10)] for _ in range(10)]

    def check_winner():
        """Check the game board for a winner."""
        for i in range(10):
            for j in range(10):
                if j <= 5 and all(board[i][j + k] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
                if i <= 5 and all(board[i + k][j] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
                if i <= 5 and j <= 5 and all(board[i + k][j + k] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
                if i <= 5 and j >= 4 and all(board[i + k][j - k] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
        return None

    layout = [
        [sg.Button("", size=(2, 1), key=(i, j)) for j in range(10)] for i in range(10)
    ]
    layout.append([sg.Button("Выход")])

    window = sg.Window("Крестики-Нолики 10x10", layout)
    current_player = "X"

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Выход"):
            break

        if isinstance(event, tuple):
            i, j = event
            if board[i][j] == "":
                board[i][j] = current_player
                window[event].update(current_player)

                winner = check_winner()
                if winner:
                    sg.popup(f"Победитель: {winner}")
                    break

                current_player = "O" if current_player == "X" else "X"

    window.close()

def play_tic_tac_toe_v2():
    """Start Tic-Tac-Toe 2.0 where computer always wins."""
    board = [["" for _ in range(10)] for _ in range(10)]

    def check_winner():
        """Check the game board for a winner."""
        for i in range(10):
            for j in range(10):
                if j <= 5 and all(board[i][j + k] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
                if i <= 5 and all(board[i + k][j] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
                if i <= 5 and j <= 5 and all(board[i + k][j + k] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
                if i <= 5 and j >= 4 and all(board[i + k][j - k] == board[i][j] != "" for k in range(5)):
                    return board[i][j]
        return None

    def computer_move():
        """Make a winning or optimal move for the computer."""
        for i in range(10):
            for j in range(10):
                if board[i][j] == "":
                    board[i][j] = "O"
                    if check_winner() == "O":
                        return i, j
                    board[i][j] = ""

        for i in range(10):
            for j in range(10):
                if board[i][j] == "":
                    board[i][j] = "X"
                    if check_winner() == "X":
                        board[i][j] = "O"
                        return i, j
                    board[i][j] = ""

        for i in range(10):
            for j in range(10):
                if board[i][j] == "":
                    return i, j

    layout = [
        [sg.Button("", size=(2, 1), key=(i, j)) for j in range(10)] for i in range(10)
    ]
    layout.append([sg.Button("Выход")])

    window = sg.Window("Крестики-Нолики 2.0", layout)
    current_player = "X"

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Выход"):
            break

        if isinstance(event, tuple):
            i, j = event
            if board[i][j] == "" and current_player == "X":
                board[i][j] = "X"
                window[event].update("X")

                winner = check_winner()
                if winner:
                    sg.popup(f"Победитель: {winner}")
                    break

                current_player = "O"
                comp_i, comp_j = computer_move()
                board[comp_i][comp_j] = "O"
                window[(comp_i, comp_j)].update("O")

                winner = check_winner()
                if winner:
                    sg.popup(f"Победитель: {winner}")
                    break

                current_player = "X"

    window.close()

if __name__ == "__main__":
    total_games = 0
    total_a = 0
    total_b = 0

    layout = [
        [sg.Text("Игры", font="Arial 26")],
        [sg.Button("Камень-Ножницы-Бумага", size=(30, 2), font="Arial 16")],
        [sg.Button("Крестики-Нолики", size=(30, 2), font="Arial 16")],
        [sg.Button("Крестики-Нолики 2.0", size=(30, 2), font="Arial 16")],
        [sg.Button("Просмотр матчей", size=(30, 2), font="Arial 16")],
        [sg.Button("Сбросить записи матчей", size=(30, 2), font="Arial 16")],
        [sg.Button("Выход", size=(30, 2), font="Arial 16")]
    ]

    main_window = sg.Window("Главное меню", layout)

    while True:
        event, _ = main_window.read()
        if event == sg.WIN_CLOSED or event == "Выход":
            break

        if event == "Камень-Ножницы-Бумага":
            play_game()
        elif event == "Крестики-Нолики":
            play_tic_tac_toe()
        elif event == "Крестики-Нолики 2.0":
            play_tic_tac_toe_v2()
        elif event == "Просмотр матчей":
            view_matches()
        elif event == "Сбросить записи матчей":
            reset_matches()

    main_window.close()

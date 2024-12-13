import PySimpleGUI as sg
import random
from time import sleep
import os

# Change theme to something lighter and pleasant
sg.theme('DarkGreen')

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
    board = [["" for _ in range(10)] for _ in range(10)]

    def check_winner():
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
                    lin = "Крестики-Нолики 1.0; Победитель:", winner
                    line = str(lin)
                    with open(FILE_PATH, 'a', encoding='utf-8') as file:
                        file.writelines(line + "\n")
                    break

                current_player = "O" if current_player == "X" else "X"

    window.close()

def play_tic_tac_toe_v2():
    board = [["" for _ in range(10)] for _ in range(10)]

    def check_winner():
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
                    lin = "Крестики-Нолики 2.0; Победил человек."
                    line = str(lin)
                    with open(FILE_PATH, 'a', encoding='utf-8') as file:
                        file.writelines(line + "\n")
                    break

                current_player = "O"
                comp_i, comp_j = computer_move()
                board[comp_i][comp_j] = "O"
                window[(comp_i, comp_j)].update("O")

                winner = check_winner()
                if winner:
                    sg.popup(f"Победитель: {winner}")
                    lin = "Крестики-Нолики 2.0; Победила машина."
                    line = str(lin)
                    with open(FILE_PATH, 'a', encoding='utf-8') as file:
                        file.writelines(line + "\n")
                    break

                current_player = "X"

    window.close()

def play_tic_tac_toe_v3():
    """Start Tic-Tac-Toe 3.0 with a 3x3 board where the computer always wins."""
    board = [["" for _ in range(3)] for _ in range(3)]

    def check_winner():
        """Check the game board for a winner."""
        for i in range(3):
            if all(board[i][j] == board[i][0] != "" for j in range(3)):
                return board[i][0]
            if all(board[j][i] == board[0][i] != "" for j in range(3)):
                return board[0][i]
        if all(board[i][i] == board[0][0] != "" for i in range(3)):
            return board[0][0]
        if all(board[i][2 - i] == board[0][2] != "" for i in range(3)):
            return board[0][2]
        return None

    def computer_move():
        """Make a winning or optimal move for the computer."""
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    if check_winner() == "O":
                        return i, j
                    board[i][j] = ""

        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    if check_winner() == "X":
                        board[i][j] = "O"
                        return i, j
                    board[i][j] = ""

        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    return i, j

    layout = [
        [sg.Button("", size=(4, 2), key=(i, j)) for j in range(3)] for i in range(3)
    ]
    layout.append([sg.Button("Выход")])

    window = sg.Window("Крестики-Нолики 3.0", layout)
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
                    lin = "Крестики-Нолики 3.0; Победил человек."
                    line = str(lin)
                    with open(FILE_PATH, 'a', encoding='utf-8') as file:
                        file.writelines(line + "\n")
                    break

                current_player = "O"
                comp_i, comp_j = computer_move()
                board[comp_i][comp_j] = "O"
                window[(comp_i, comp_j)].update("O")

                winner = check_winner()
                if winner:
                    sg.popup(f"Победитель: {winner}")
                    lin = "Крестики-Нолики 3.0; Победила машина."
                    line = str(lin)
                    with open(FILE_PATH, 'a', encoding='utf-8') as file:
                        file.writelines(line + "\n")
                    break

                current_player = "X"

    window.close()

def create_empty_board():
    return [[" " for _ in range(10)] for _ in range(10)]

# Размещение кораблей
def place_ships(board, player_name):
    sg.popup(f"{player_name}, разместите свои корабли.")
    ships = [5, 4, 3, 3, 2]  # Длины кораблей

    for ship_length in ships:
        placed = False
        while not placed:
            layout = [
                [sg.Text(f"Ваше поле (разместите корабль длиной {ship_length}):")],
                [sg.Column([[sg.Button(" ", key=(x, y), size=(2, 1)) for y in range(10)] for x in range(10)])],
                [sg.Button("Готово")]
            ]
            window = sg.Window(f"Размещение кораблей {player_name}", layout, finalize=True)

            def update_board_display():
                """Обновляет отображение поля игрока."""
                for x in range(10):
                    for y in range(10):
                        button_text = " " if board[x][y] == " " else "S"
                        window[(x, y)].update(button_text)

            update_board_display()

            while True:
                event, _ = window.read()

                if event in (sg.WIN_CLOSED, "Готово"):
                    window.close()
                    return
                if isinstance(event, tuple):  # Нажатие на ячейку
                    x, y = event
                    orientation_layout = [
                        [sg.Text("Выберите ориентацию:")],
                        [sg.Button("Горизонтально"), sg.Button("Вертикально")]
                    ]
                    orientation_window = sg.Window("Ориентация корабля", orientation_layout, finalize=True)
                    orientation_event, _ = orientation_window.read()
                    orientation_window.close()

                    if orientation_event == "Горизонтально":
                        orientation = "h"
                    elif orientation_event == "Вертикально":
                        orientation = "v"
                    else:
                        continue

                    # Проверка размещения корабля
                    if orientation == "h" and y + ship_length <= 10 and all(board[x][y + i] == " " for i in range(ship_length)):
                        for i in range(ship_length):
                            board[x][y + i] = "S"
                        placed = True
                    elif orientation == "v" and x + ship_length <= 10 and all(board[x + i][y] == " " for i in range(ship_length)):
                        for i in range(ship_length):
                            board[x + i][y] = "S"
                        placed = True
                    else:
                        sg.popup("Корабль нельзя разместить здесь. Попробуйте снова.")

                    # Обновление поля после размещения корабля
                    update_board_display()
                    if placed:
                        break

            window.close()


# Проверка на победу
def check_winner(board):
    return all(cell != "S" for row in board for cell in row)

def take_turn(board, enemy_board, player, player_name, enemy_name, turn_history):
    sg.popup(f"Ход {player_name}.")

    layout = [
        [sg.Text("Ваше поле:")],
        [sg.Column([[sg.Button(" ", key=(x, y), size=(2, 1)) for y in range(10)] for x in range(10)])],
        [sg.Button("Обновить")],
        [sg.Text("Поле противника:")],
        [sg.Column([[sg.Button(" ", key=("enemy", x, y), size=(2, 1)) for y in range(10)] for x in range(10)])],
        [sg.Button("Сдаться")]
    ]

    window = sg.Window(f"Ход {player_name}", layout, finalize=True)

    def update_display():
        """Обновляет отображение обоих полей."""
        for x in range(10):
            for y in range(10):
                # Обновление поля игрока
                button_text = " "
                if board[x][y] == "S":
                    button_text = "S"
                elif board[x][y] == "H":
                    button_text = "X"
                elif board[x][y] == "M":
                    button_text = "O"
                window[(x, y)].update(button_text)

                # Обновление поля противника
                enemy_button_text = " "
                if enemy_board[x][y] == "H":
                    enemy_button_text = "X"
                elif enemy_board[x][y] == "M":
                    enemy_button_text = "O"
                window[("enemy", x, y)].update(enemy_button_text)

    update_display()

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "Сдаться"):
            sg.popup(f"{player_name} сдался!")
            window.close()
            return None  # Сдача

        if event == "Обновить":
            update_display()
            continue

        if isinstance(event, tuple) and event[0] == "enemy":
            _, x, y = event
            if enemy_board[x][y] == "S":  # Попадание
                enemy_board[x][y] = "H"
                turn_history[player].append(("Попадание", x, y))
                sg.popup("Попадание!")
                update_display()
                return True  # Ход остаётся у игрока
            elif enemy_board[x][y] == " ":
                enemy_board[x][y] = "M"  # Мимо
                turn_history[player].append(("Промах", x, y))
                sg.popup("Мимо!")
                update_display()
                return False  # Ход передаётся
            else:
                sg.popup("Вы уже стреляли сюда.")
                update_display()

    window.close()



def play_battleship_v2():
    while True:  # Позволяет начать новую игру после завершения предыдущей
        player1_board = create_empty_board()
        player2_board = create_empty_board()

        turn_history = {1: [], 2: []}  # Хранение истории ходов

        # Запрашиваем имена игроков
        layout = [
            [sg.Text("Введите имя Игрока 1:"), sg.Input(key="player1")],
            [sg.Text("Введите имя Игрока 2:"), sg.Input(key="player2")],
            [sg.Button("Начать игру"), sg.Button("Выход")]
        ]

        window = sg.Window("Морской бой - Имена игроков", layout)
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Выход"):
            window.close()
            return

        player1_name = values["player1"] if values["player1"] else "Игрок 1"
        player2_name = values["player2"] if values["player2"] else "Игрок 2"
        window.close()

        # Размещение кораблей
        place_ships(player1_board, player1_name)
        place_ships(player2_board, player2_name)

        # Игра начинается
        current_player = 1
        winner = None

        while True:
            if current_player == 1:
                player_board = player1_board
                enemy_board = player2_board
                player_name = player1_name
                enemy_name = player2_name
            else:
                player_board = player2_board
                enemy_board = player1_board
                player_name = player2_name
                enemy_name = player1_name

            # Ход текущего игрока
            hit = take_turn(player_board, enemy_board, current_player, player_name, enemy_name, turn_history)
            if hit is None:  # Игрок сдался
                winner = enemy_name
                sg.popup(f"{player_name} сдался! Победитель: {winner}")
                break
            elif not hit:  # Если игрок пропускает ход
                current_player = 2 if current_player == 1 else 1

            # Проверка на победителя
            if all(cell != "S" for row in enemy_board for cell in row):  # Все корабли уничтожены
                winner = player_name
                sg.popup(f"Победитель: {winner}")
                break

        # Предлагаем начать новую игру
        if sg.popup_yes_no("Хотите сыграть ещё раз?") == "No":
            break

# Создание пустого игрового поля
def create_empty_board():
    return [[" " for _ in range(10)] for _ in range(10)]

# Автоматическая расстановка кораблей
def auto_place_ships(board):
    ships = [5, 4, 3, 3, 2]  # Длины кораблей

    for ship_length in ships:
        placed = False
        while not placed:
            orientation = random.choice(["h", "v"])  # Горизонтально или вертикально
            x, y = random.randint(0, 9), random.randint(0, 9)

            if orientation == "h" and y + ship_length <= 10 and all(board[x][y + i] == " " for i in range(ship_length)):
                for i in range(ship_length):
                    board[x][y + i] = "S"
                placed = True
            elif orientation == "v" and x + ship_length <= 10 and all(board[x + i][y] == " " for i in range(ship_length)):
                for i in range(ship_length):
                    board[x + i][y] = "S"
                placed = True

# Размещение кораблей игроком
def place_ships(board, player_name):
    sg.popup(f"{player_name}, разместите свои корабли.")
    ships = [5, 4, 3, 3, 2]  # Длины кораблей

    for ship_length in ships:
        placed = False
        while not placed:
            layout = [
                [sg.Text(f"Ваше поле (разместите корабль длиной {ship_length}):")],
                [sg.Column([[sg.Button(" ", key=(x, y), size=(2, 1)) for y in range(10)] for x in range(10)])],
                [sg.Button("Готово")]
            ]
            window = sg.Window(f"Размещение кораблей {player_name}", layout, finalize=True)

            def update_board_display():
                for x in range(10):
                    for y in range(10):
                        button_text = " " if board[x][y] == " " else "S"
                        window[(x, y)].update(button_text)

            update_board_display()

            while True:
                event, _ = window.read()

                if event in (sg.WIN_CLOSED, "Готово"):
                    window.close()
                    return
                if isinstance(event, tuple):  # Нажатие на ячейку
                    x, y = event
                    orientation_layout = [
                        [sg.Text("Выберите ориентацию:")],
                        [sg.Button("Горизонтально"), sg.Button("Вертикально")]
                    ]
                    orientation_window = sg.Window("Ориентация корабля", orientation_layout, finalize=True)
                    orientation_event, _ = orientation_window.read()
                    orientation_window.close()

                    orientation = "h" if orientation_event == "Горизонтально" else "v"

                    # Проверка размещения
                    if orientation == "h" and y + ship_length <= 10 and all(board[x][y + i] == " " for i in range(ship_length)):
                        for i in range(ship_length):
                            board[x][y + i] = "S"
                        placed = True
                    elif orientation == "v" and x + ship_length <= 10 and all(board[x + i][y] == " " for i in range(ship_length)):
                        for i in range(ship_length):
                            board[x + i][y] = "S"
                        placed = True
                    else:
                        sg.popup("Корабль нельзя разместить здесь. Попробуйте снова.")

                    update_board_display()
                    if placed:
                        break

            window.close()

# Проверка на победу
def check_winner(board):
    return all(cell != "S" for row in board for cell in row)

# Ход компьютера
def computer_turn(board):
    while True:
        x, y = random.randint(0, 9), random.randint(0, 9)
        if board[x][y] in (" ", "S"):  # Нельзя стрелять в уже атакованные ячейки
            if board[x][y] == "S":
                board[x][y] = "H"
                return True  # Попадание
            elif board[x][y] == " ":
                board[x][y] = "M"
                return False  # Промах

# Ход игрока
def take_turn(board, enemy_board, player_name):
    sg.popup(f"Ход {player_name}.")

    layout = [
        [sg.Text("Ваше поле:")],
        [sg.Column([[sg.Button(" ", key=(x, y), size=(2, 1)) for y in range(10)] for x in range(10)])],
        [sg.Button("Обновить")],
        [sg.Text("Поле противника:")],
        [sg.Column([[sg.Button(" ", key=("enemy", x, y), size=(2, 1)) for y in range(10)] for x in range(10)])],
        [sg.Button("Сдаться")]
    ]

    window = sg.Window(f"Ход {player_name}", layout, finalize=True)

    def update_display():
        for x in range(10):
            for y in range(10):
                button_text = " " if board[x][y] == " " else ("X" if board[x][y] == "H" else "O" if board[x][y] == "M" else "S")
                window[(x, y)].update(button_text)

                enemy_button_text = " " if enemy_board[x][y] == " " else ("X" if enemy_board[x][y] == "H" else "O" if enemy_board[x][y] == "M" else " ")
                window[("enemy", x, y)].update(enemy_button_text)

    update_display()

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "Сдаться"):
            window.close()
            return None  # Игрок сдался

        if isinstance(event, tuple) and event[0] == "enemy":
            _, x, y = event
            if enemy_board[x][y] == "S":
                enemy_board[x][y] = "H"
                sg.popup("Попадание!")
                update_display()
                return True
            elif enemy_board[x][y] == " ":
                enemy_board[x][y] = "M"
                sg.popup("Мимо!")
                update_display()
                return False
            else:
                sg.popup("Вы уже стреляли сюда.")

    window.close()

# Основной игровой цикл
def play_battleship_v3():
    player_board = create_empty_board()
    computer_board = create_empty_board()

    place_ships(player_board, "Игрок")
    auto_place_ships(computer_board)

    current_player = "player"

    while True:
        if current_player == "player":
            hit = take_turn(player_board, computer_board, "Игрок")
            if hit is None or check_winner(computer_board):
                sg.popup("Вы победили!")
                break
            elif not hit:
                current_player = "computer"
        else:
            hit = computer_turn(player_board)
            if check_winner(player_board):
                sg.popup("Компьютер победил!")
                break
            elif not hit:
                current_player = "player"

if __name__ == "__main__":
    total_games = 0
    total_a = 0
    total_b = 0

    layout = [
        [sg.Text("Игры", font="Arial 26")],
        [sg.Button("Камень-Ножницы-Бумага", size=(30, 2), font="Arial 16")],
        [sg.Button("Крестики-Нолики", size=(30, 2), font="Arial 16")],
        [sg.Button("Крестики-Нолики 2.0", size=(30, 2), font="Arial 16")],
        [sg.Button("Крестики-Нолики 3.0", size=(30, 2), font="Arial 16")],
        [sg.Button("Морской бой v2", size=(30,2), font="Arial 16")],
        [sg.Button("Морской бой v3", size=(30,2), font="Arial 16")],
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
        elif event == "Крестики-Нолики 3.0":
            play_tic_tac_toe_v3()
        elif event == "Морской бой v2":
            play_battleship_v2()
        elif event == "Морской бой v3":
            play_battleship_v3()
        elif event == "Просмотр матчей":
            view_matches()
        elif event == "Сбросить записи матчей":
            reset_matches()

    main_window.close()

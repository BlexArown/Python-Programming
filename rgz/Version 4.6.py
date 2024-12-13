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

def play_game():
    """Play Rock-Paper-Scissors."""
    choices = {1: "Камень", 2: "Бумага", 3: "Ножницы"}

    layout = [
        [sg.Text("Камень-Ножницы-Бумага", font="Arial 16")],
        [sg.Button("Камень"), sg.Button("Бумага"), sg.Button("Ножницы")],
        [sg.Button("Выход")]
    ]

    window = sg.Window("Камень-Ножницы-Бумага", layout)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Выход"):
            break

        user_choice = None
        if event == "Камень":
            user_choice = ROCK
        elif event == "Бумага":
            user_choice = PAPER
        elif event == "Ножницы":
            user_choice = SCISSORS

        if user_choice:
            computer_choice = random.randint(1, 3)
            sg.popup(f"Вы выбрали: {choices[user_choice]}\nКомпьютер выбрал: {choices[computer_choice]}")

    window.close()

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

import PySimpleGUI as sg

import random
import PySimpleGUI as sg

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

def main_menu():
    layout = [
        [sg.Button("Камень-Ножницы-Бумага")],
        [sg.Button("Крестики-Нолики 3.0")],
        [sg.Button("Просмотр матчей")],
        [sg.Button("Сброс матчей")],
        [sg.Button("Морской бой v2")],
        [sg.Button("Выход")]
    ]
    window = sg.Window("Главное меню", layout)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Выход"):
            break
        elif event == "Камень-Ножницы-Бумага":
            play_game()
        elif event == "Крестики-Нолики 3.0":
            play_tic_tac_toe_v3()
        elif event == "Просмотр матчей":
            view_matches()
        elif event == "Сброс матчей":
            reset_matches()
        elif event == "Морской бой v2":
            play_battleship_v3()

    window.close()

if __name__ == "__main__":
    main_menu()

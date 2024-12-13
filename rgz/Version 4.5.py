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
        elif event == "Просмотр матчей":
            view_matches()
        elif event == "Сбросить записи матчей":
            reset_matches()

    main_window.close()

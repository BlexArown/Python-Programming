import pygame
import random
from pygame.locals import *

# -------------------- EASY (8x8) --------------------

def start_game_easy():
    board = [[0 for _ in range(8)] for _ in range(8)]
    add_new_tile_easy(board)
    add_new_tile_easy(board)
    return board

def add_new_tile_easy(board):
    empty_cells = [(i, j) for i in range(8) for j in range(8) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def is_game_over_easy(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                return False
            if j < 7 and board[i][j] == board[i][j + 1]:
                return False
            if i < 7 and board[i][j] == board[i + 1][j]:
                return False
    return True

def move_easy(board, direction):
    points = 0
    if direction == 'up':
        board = transpose_easy(board)
        for i in range(8):
            board[i], row_points = merge_tiles_easy(board[i])
            points += row_points
        board = transpose_easy(board)
    elif direction == 'down':
        board = transpose_easy(board)
        for i in range(8):
            board[i], row_points = merge_tiles_easy(board[i][::-1])
            board[i] = board[i][::-1]
            points += row_points
        board = transpose_easy(board)
    elif direction == 'left':
        for i in range(8):
            board[i], row_points = merge_tiles_easy(board[i])
            points += row_points
    elif direction == 'right':
        for i in range(8):
            board[i], row_points = merge_tiles_easy(board[i][::-1])
            board[i] = board[i][::-1]
            points += row_points
    add_new_tile_easy(board)
    return board, points

def transpose_easy(board):
    return [[board[j][i] for j in range(8)] for i in range(8)]

def merge_tiles_easy(row):
    row = [tile for tile in row if tile != 0]
    new_row = []
    points = 0
    skip = False
    for i in range(len(row) - 1):
        if skip:
            skip = False
            continue
        if row[i] == row[i + 1]:
            new_value = row[i] * 2
            new_row.append(new_value)
            points += new_value  # Добавляем очки
            skip = True
        else:
            new_row.append(row[i])
    if not skip and len(row) > 0:
        new_row.append(row[-1])
    new_row += [0] * (8 - len(new_row))
    return new_row, points

# -------------------- MEDIUM (6x6) --------------------

def start_game_medium():
    board = [[0 for _ in range(6)] for _ in range(6)]
    add_new_tile_medium(board)
    add_new_tile_medium(board)
    return board

def add_new_tile_medium(board):
    empty_cells = [(i, j) for i in range(6) for j in range(6) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def is_game_over_medium(board):
    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                return False
            if j < 5 and board[i][j] == board[i][j + 1]:
                return False
            if i < 5 and board[i][j] == board[i + 1][j]:
                return False
    return True

def move_medium(board, direction):
    total_points = 0
    if direction == 'up':
        board = transpose_medium(board)
        for i in range(6):
            board[i], row_points = merge_tiles_medium(board[i])
            total_points += row_points
        board = transpose_medium(board)
    elif direction == 'down':
        board = transpose_medium(board)
        for i in range(6):
            board[i], row_points = merge_tiles_medium(board[i][::-1])
            board[i] = board[i][::-1]
            total_points += row_points
        board = transpose_medium(board)
    elif direction == 'left':
        for i in range(6):
            board[i], row_points = merge_tiles_medium(board[i])
            total_points += row_points
    elif direction == 'right':
        for i in range(6):
            board[i], row_points = merge_tiles_medium(board[i][::-1])
            board[i] = board[i][::-1]
            total_points += row_points
    add_new_tile_medium(board)
    return board, total_points

def transpose_medium(board):
    return [[board[j][i] for j in range(6)] for i in range(6)]

def merge_tiles_medium(row):
    row = [tile for tile in row if tile != 0]
    new_row = []
    points = 0
    skip = False
    for i in range(len(row) - 1):
        if skip:
            skip = False
            continue
        if row[i] == row[i + 1]:
            new_row.append(row[i] * 2)
            points += row[i] * 2
            skip = True
        else:
            new_row.append(row[i])
    if not skip and len(row) > 0:
        new_row.append(row[-1])
    new_row += [0] * (6 - len(new_row))
    return new_row, points


# -------------------- HARD (4x4) --------------------

def start_game_hard():
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile_hard(board)
    add_new_tile_hard(board)
    return board

def add_new_tile_hard(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def is_game_over_hard(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
    return True

def move_hard(board, direction):
    total_points = 0
    if direction == 'up':
        board = transpose_hard(board)
        for i in range(4):
            board[i], row_points = merge_tiles_hard(board[i])
            total_points += row_points
        board = transpose_hard(board)
    elif direction == 'down':
        board = transpose_hard(board)
        for i in range(4):
            board[i], row_points = merge_tiles_hard(board[i][::-1])
            board[i] = board[i][::-1]
            total_points += row_points
        board = transpose_hard(board)
    elif direction == 'left':
        for i in range(4):
            board[i], row_points = merge_tiles_hard(board[i])
            total_points += row_points
    elif direction == 'right':
        for i in range(4):
            board[i], row_points = merge_tiles_hard(board[i][::-1])
            board[i] = board[i][::-1]
            total_points += row_points
    add_new_tile_hard(board)
    return board, total_points


def transpose_hard(board):
    return [[board[j][i] for j in range(4)] for i in range(4)]

def merge_tiles_hard(row):
    row = [tile for tile in row if tile != 0]
    new_row = []
    points = 0
    skip = False
    for i in range(len(row) - 1):
        if skip:
            skip = False
            continue
        if row[i] == row[i + 1]:
            new_row.append(row[i] * 2)
            points += row[i] * 2  # Добавляем очки за объединение
            skip = True
        else:
            new_row.append(row[i])
    if not skip and len(row) > 0:
        new_row.append(row[-1])
    new_row += [0] * (4 - len(new_row))
    return new_row, points


# -------------------- MAIN GAME LOGIC --------------------

def draw_menu(screen, font):
    screen.fill((187, 173, 160))
    
    # Текст заголовка
    title_surface = font.render("Выберите сложность", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(200, 50))
    screen.blit(title_surface, title_rect)

    # Кнопки
    buttons = [
        {"text": "Easy (8x8)", "rect": pygame.Rect(100, 100, 200, 50), "color": (135, 206, 250), "difficulty": "easy"},
        {"text": "Medium (6x6)", "rect": pygame.Rect(100, 175, 200, 50), "color": (255, 165, 0), "difficulty": "medium"},
        {"text": "Hard (4x4)", "rect": pygame.Rect(100, 250, 200, 50), "color": (255, 99, 71), "difficulty": "hard"},
    ]

    for button in buttons:
        pygame.draw.rect(screen, button["color"], button["rect"])
        text_surface = font.render(button["text"], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button["rect"].center)
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
    return buttons

def draw_victory_buttons(screen, font, screen_width, screen_height):
    button_width = 150
    button_height = 50
    button_margin = 20

    # Расчёт положения кнопок
    center_x = screen_width // 2
    center_y = screen_height // 2
    continue_button_rect = pygame.Rect(
        center_x - button_width - button_margin, 
        center_y, 
        button_width, 
        button_height
    )
    quit_button_rect = pygame.Rect(
        center_x + button_margin, 
        center_y, 
        button_width, 
        button_height
    )

    # Рисуем кнопки
    pygame.draw.rect(screen, (76, 187, 23), continue_button_rect)  # Зелёная кнопка
    pygame.draw.rect(screen, (200, 50, 50), quit_button_rect)      # Красная кнопка

    # Текст на кнопках
    continue_text = font.render("Продолжить", True, (255, 255, 255))
    quit_text = font.render("Закончить", True, (255, 255, 255))

    screen.blit(continue_text, continue_text.get_rect(center=continue_button_rect.center))
    screen.blit(quit_text, quit_text.get_rect(center=quit_button_rect.center))

    pygame.display.flip()
    return continue_button_rect, quit_button_rect


def handle_menu_click(buttons, pos):
    for button in buttons:
        if button["rect"].collidepoint(pos):
            return button["difficulty"]
    return None


def check_win_condition(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def show_victory_screen(screen, font, score):
    # Задний фон
    screen.fill((0, 0, 0))

    # Текст победы
    victory_text = font.render("Вы достигли 2048!", True, (255, 255, 255))
    score_text = font.render(f"Ваш итог: {int(score)} очков", True, (255, 255, 255))
    continue_text = font.render("Продолжить? (Y/N)", True, (255, 255, 255))

    # Рисуем текст
    screen.blit(victory_text, victory_text.get_rect(center=(200, 150)))
    screen.blit(score_text, score_text.get_rect(center=(200, 200)))
    screen.blit(continue_text, continue_text.get_rect(center=(200, 250)))

    pygame.display.flip()



def run_game(start_game, add_new_tile, move, is_game_over, board_size, score_multiplier):
    pygame.init()
    tile_size = 50
    margin = 5
    score_area_height = 50
    button_area_height = 50

    screen_width = (tile_size + margin) * board_size + margin
    screen_height = screen_width + score_area_height + button_area_height
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("2048 Game")

    board = start_game()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    score = 0
    running = True
    surrender = False

    while running:
        screen.fill((187, 173, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board, points = move(board, 'up')
                elif event.key == pygame.K_DOWN:
                    board, points = move(board, 'down')
                elif event.key == pygame.K_LEFT:
                    board, points = move(board, 'left')
                elif event.key == pygame.K_RIGHT:
                    board, points = move(board, 'right')
                score += points * score_multiplier

            if event.type == pygame.MOUSEBUTTONDOWN:
                if surrender_button.collidepoint(event.pos):
                    surrender = True
                    running = False

        # Проверка на плитку 2048
        if check_win_condition(board):
            continue_button, quit_button = draw_modal_window(screen, font, screen_width, screen_height, "Вы достигли 2048. Продолжить?")
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if continue_button.collidepoint(event.pos):
                            waiting = False  # Продолжить игру
                        elif quit_button.collidepoint(event.pos):
                            show_results_window(screen, font, screen_width, screen_height, True, score, required_score=10000)
                            pygame.quit()
                            return

        # Проверка завершения игры
        if is_game_over(board):
            show_results_window(screen, font, screen_width, screen_height, False, score, required_score=10000)
            pygame.quit()
            return

        draw_board(screen, board, font, tile_size, margin, score_area_height)
        draw_score(screen, font, score, board_size, screen_width, score_area_height)
        surrender_button = draw_surrender_button(screen, font, screen_width, screen_height, button_area_height)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    if surrender:
        main()





def draw_board(screen, board, font, tile_size, margin, score_area_height):
    for row in range(len(board)):
        for col in range(len(board[row])):
            tile_value = board[row][col]
            x = margin + col * (tile_size + margin)
            y = margin + row * (tile_size + margin) + score_area_height

            # Цвет плитки в зависимости от её значения
            tile_color = (205, 193, 180) if tile_value == 0 else (238, 228, 218)
            pygame.draw.rect(screen, tile_color, (x, y, tile_size, tile_size), border_radius=5)

            # Текст на плитке
            if tile_value > 0:
                text = font.render(str(tile_value), True, (119, 110, 101))
                text_rect = text.get_rect(center=(x + tile_size // 2, y + tile_size // 2))
                screen.blit(text, text_rect)

def check_win_condition(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def run_game(start_game, add_new_tile, move, is_game_over, board_size, score_multiplier):
    pygame.init()
    tile_size = 50
    margin = 5
    score_area_height = 50
    button_area_height = 50

    screen_width = (tile_size + margin) * board_size + margin
    screen_height = screen_width + score_area_height + button_area_height
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("2048 Game")

    board = start_game()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    score = 0
    running = True
    reached_2048 = False

    def draw_board_with_highlight(screen, board, font, tile_size, margin, score_area_height):
        colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            2048: (255, 215, 0),  # Золотой цвет для плитки 2048
        }

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                color = colors.get(value, (60, 58, 50))
                x = margin + col * (tile_size + margin)
                y = margin + row * (tile_size + margin) + score_area_height

                if value == 2048:
                    pygame.draw.rect(screen, (255, 0, 0), (x - 2, y - 2, tile_size + 4, tile_size + 4), border_radius=8)
                pygame.draw.rect(screen, color, (x, y, tile_size, tile_size), border_radius=8)

                if value != 0:
                    text = font.render(str(value), True, (0, 0, 0) if value < 2048 else (255, 255, 255))
                    screen.blit(text, text.get_rect(center=(x + tile_size // 2, y + tile_size // 2)))

    def draw_score(screen, font, score, screen_width, score_area_height):
        text_surface = font.render(f"Очки: {int(score)}", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(screen_width // 2, score_area_height // 2))
        screen.blit(text_surface, text_rect)

    def draw_exit_button(screen, font, screen_width, screen_height, button_area_height):
        """Кнопка 'Выйти' для возврата в меню."""
        button_width = 150
        button_height = 50

        # Позиционируем кнопку внизу
        button_x = (screen_width - button_width) // 2
        button_y = screen_height - button_area_height + 150

        button_color = (70, 130, 180)
        text_color = (255, 255, 255)

        exit_button = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_color, exit_button)

        text_surface = font.render("Выйти", True, text_color)
        text_rect = text_surface.get_rect(center=exit_button.center)
        screen.blit(text_surface, text_rect)

        return exit_button

    def draw_surrender_button(screen, font, screen_width, screen_height, button_area_height):
        # Размер и позиция кнопки
        button_width = screen_width // 3
        button_height = button_area_height - 10
        button_x = (screen_width - button_width) // 2
        button_y = screen_height - button_area_height + 5

        # Цвет кнопки и текста
        button_color = (144, 238, 144)  # Светло-зелёный
        text_color = (0, 0, 0)

        # Рисуем прямоугольник кнопки
        surrender_button = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_color, surrender_button)

        # Добавляем текст "Сдаться"
        text_surface = font.render("Сдаться", True, text_color)
        text_rect = text_surface.get_rect(center=surrender_button.center)
        screen.blit(text_surface, text_rect)

        return surrender_button

    def draw_modal_window(screen, font, screen_width, screen_height, text):
        modal_width = 500
        modal_height = 250
        modal_rect = pygame.Rect(
            (screen_width - modal_width) // 2,
            (screen_height - modal_height) // 2,
            modal_width,
            modal_height
        )

        pygame.draw.rect(screen, (50, 50, 50), modal_rect)
        pygame.draw.rect(screen, (255, 255, 255), modal_rect, width=2)

        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, text_surface.get_rect(center=(modal_rect.centerx, modal_rect.top + 50)))

        button_width = 150
        button_height = 60
        button_margin = 30

        continue_button = pygame.Rect(
            modal_rect.left + button_margin,
            modal_rect.bottom - button_height - button_margin,
            button_width,
            button_height
        )
        quit_button = pygame.Rect(
            modal_rect.centerx - button_width // 2,
            modal_rect.bottom - button_height - button_margin,
            button_width,
            button_height
        )
        exit_button = pygame.Rect(
            modal_rect.right - button_width - button_margin,
            modal_rect.bottom - button_height - button_margin,
            button_width,
            button_height
        )

        pygame.draw.rect(screen, (76, 187, 23), continue_button)
        pygame.draw.rect(screen, (200, 50, 50), quit_button)
        pygame.draw.rect(screen, (70, 130, 180), exit_button)

        continue_text = font.render("Продолжить", True, (255, 255, 255))
        quit_text = font.render("Закончить", True, (255, 255, 255))
        exit_text = font.render("Выйти", True, (255, 255, 255))

        screen.blit(continue_text, continue_text.get_rect(center=continue_button.center))
        screen.blit(quit_text, quit_text.get_rect(center=quit_button.center))
        screen.blit(exit_text, exit_text.get_rect(center=exit_button.center))

        pygame.display.flip()
        return continue_button, quit_button, exit_button

    def show_results_window(screen, font, screen_width, screen_height, reached_2048, current_score, required_score):
        modal_width = 500
        modal_height = 300
        modal_rect = pygame.Rect(
            (screen_width - modal_width) // 2,
            (screen_height - modal_height) // 2,
            modal_width,
            modal_height
        )

        pygame.draw.rect(screen, (50, 50, 50), modal_rect)
        pygame.draw.rect(screen, (255, 255, 255), modal_rect, width=2)

        text_lines = [
            f"Достигли 2048: {'Да' if reached_2048 else 'Нет'}",
            f"Победа по очкам: {current_score}/{required_score}",
        ]
        result_text = "Поздравляю вас, вы одержали верх!" if reached_2048 and current_score >= required_score else "Вы частично проиграли, всё бывает."
        text_lines.append(result_text)

        for i, line in enumerate(text_lines):
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, text_surface.get_rect(center=(modal_rect.centerx, modal_rect.top + 60 + i * 40)))

        pygame.display.flip()
        pygame.time.wait(3000)

    while running:
        screen.fill((187, 173, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board, points = move(board, 'up')
                elif event.key == pygame.K_DOWN:
                    board, points = move(board, 'down')
                elif event.key == pygame.K_LEFT:
                    board, points = move(board, 'left')
                elif event.key == pygame.K_RIGHT:
                    board, points = move(board, 'right')
                score += points * score_multiplier
            if event.type == pygame.MOUSEBUTTONDOWN:
                if surrender_button.collidepoint(event.pos):
                    surrender = True
                    running = False

        if 2048 in sum(board, []):
            if not reached_2048:
                reached_2048 = True
                continue_button, quit_button, exit_button = draw_modal_window(screen, font, screen_width, screen_height, "Вы достигли 2048!")
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if continue_button.collidepoint(event.pos):
                                waiting = False  # Продолжаем игру
                            elif quit_button.collidepoint(event.pos):
                                show_results_window(screen, font, screen_width, screen_height, True, score, required_score=10000)
                                pygame.quit()
                                return
                            elif exit_button.collidepoint(event.pos):
                                return  # Возврат в главное меню

        if is_game_over(board):
            show_results_window(screen, font, screen_width, screen_height, reached_2048, score, required_score=10000)
            pygame.quit()
            return

        draw_board_with_highlight(screen, board, font, tile_size, margin, score_area_height)
        draw_score(screen, font, score, screen_width, score_area_height)

        # Отображаем кнопку "Выйти"
        exit_button = draw_exit_button(screen, font, screen_width, screen_height, button_area_height)

        # Проверка нажатия на кнопку "Выйти"
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    pygame.quit()  # Закрытие игры и возврат в меню

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    if surrender:
        main()

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("2048 Game")

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    running = True
    selected_difficulty = None

    while running:
        if selected_difficulty is None:
            buttons = draw_menu(screen, font)
        else:
            # Выбор режима
            if selected_difficulty == "easy":
                run_game(start_game_easy, add_new_tile_easy, move_easy, is_game_over_easy, 8, 3)
            elif selected_difficulty == "medium":
                run_game(start_game_medium, add_new_tile_medium, move_medium, is_game_over_medium, 6, 1.5)
            elif selected_difficulty == "hard":
                run_game(start_game_hard, add_new_tile_hard, move_hard, is_game_over_hard, 4, 0.3)
            running = False  # После выхода из игры завершить главный цикл

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and selected_difficulty is None:
                selected_difficulty = handle_menu_click(buttons, event.pos)

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
import random

# Инициализация игрового поля
def start_game():
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Добавление нового тайла на поле
def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

# Проверка, завершена ли игра
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
    return True

# Реализация логики игры
def move(board, direction):
    if direction == 'up':
        board = transpose(board)
        for i in range(4):
            board[i] = merge_tiles(board[i])
        board = transpose(board)
    elif direction == 'down':
        board = transpose(board)
        for i in range(4):
            board[i] = merge_tiles(board[i][::-1])[::-1]
        board = transpose(board)
    elif direction == 'left':
        for i in range(4):
            board[i] = merge_tiles(board[i])
    elif direction == 'right':
        for i in range(4):
            board[i] = merge_tiles(board[i][::-1])[::-1]
    add_new_tile(board)
    return board

def transpose(board):
    return [[board[j][i] for j in range(4)] for i in range(4)]

def merge_tiles(row):
    row = [tile for tile in row if tile != 0]
    new_row = []
    skip = False
    for i in range(len(row) - 1):
        if skip:
            skip = False
            continue
        if row[i] == row[i + 1]:
            new_row.append(row[i] * 2)
            skip = True
        else:
            new_row.append(row[i])
    if not skip and len(row) > 0:
        new_row.append(row[-1])
    new_row += [0] * (4 - len(new_row))
    return new_row

# Инициализация Pygame
pygame.init()

# Параметры окна
SIZE = 4
TILE_SIZE = 100
WINDOW_SIZE = SIZE * TILE_SIZE
FONT_SIZE = 40
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Создание окна
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("2048")
font = pygame.font.Font(None, FONT_SIZE)

def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for i in range(SIZE):
        for j in range(SIZE):
            value = board[i][j]
            color = TILE_COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(
                screen,
                color,
                (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE),
            )
            if value != 0:
                text = font.render(str(value), True, (119, 110, 101))
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

    pygame.display.flip()

def main():
    board = start_game()
    running = True

    while running:
        draw_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board = move(board, 'up')
                elif event.key == pygame.K_DOWN:
                    board = move(board, 'down')
                elif event.key == pygame.K_LEFT:
                    board = move(board, 'left')
                elif event.key == pygame.K_RIGHT:
                    board = move(board, 'right')

                if is_game_over(board):
                    print("Game Over")
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()

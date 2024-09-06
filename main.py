import pygame
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('2048')

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (187, 173, 160)
COLORS = {
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
    2048: (237, 194, 46),
}

# 初始化游戏状态
board = [[0] * 4 for _ in range(4)]

def add_new_tile():
    empty_tiles = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    r, c = random.choice(empty_tiles)
    board[r][c] = random.choice([2, 4])

def draw_board():
    screen.fill(GRAY)
    for r in range(4):
        for c in range(4):
            value = board[r][c]
            color = COLORS.get(value, BLACK)
            pygame.draw.rect(screen, color, (c * 100 + 10, r * 100 + 10, 80, 80))
            if value:
                font = pygame.font.Font(None, 55)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(c * 100 + 50, r * 100 + 50))
                screen.blit(text, text_rect)

def move_left():
    for r in range(4):
        new_row = [i for i in board[r] if i != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [i for i in new_row if i != 0]
        board[r] = new_row + [0] * (4 - len(new_row))

def move_right():
    for r in range(4):
        new_row = [i for i in board[r] if i != 0]
        for i in range(len(new_row) - 1, 0, -1):
            if new_row[i] == new_row[i - 1]:
                new_row[i] *= 2
                new_row[i - 1] = 0
        new_row = [i for i in new_row if i != 0]
        board[r] = [0] * (4 - len(new_row)) + new_row

def move_up():
    for c in range(4):
        new_col = [board[r][c] for r in range(4) if board[r][c] != 0]
        for i in range(len(new_col) - 1):
            if new_col[i] == new_col[i + 1]:
                new_col[i] *= 2
                new_col[i + 1] = 0
        new_col = [i for i in new_col if i != 0]
        for r in range(4):
            board[r][c] = new_col[r] if r < len(new_col) else 0

def move_down():
    for c in range(4):
        new_col = [board[r][c] for r in range(4) if board[r][c] != 0]
        for i in range(len(new_col) - 1, 0, -1):
            if new_col[i] == new_col[i - 1]:
                new_col[i] *= 2
                new_col[i - 1] = 0
        new_col = [i for i in new_col if i != 0]
        for r in range(4):
            board[r][c] = new_col[r - (4 - len(new_col))] if r >= (4 - len(new_col)) else 0


# 游戏主循环
running = True
add_new_tile()
add_new_tile()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
            add_new_tile()
    draw_board()
    pygame.display.flip()

pygame.quit()

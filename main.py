from itertools import product

import pygame
import sys

from config import *

# Инициализация pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Создание окна
pygame.display.set_caption("Go Game")  # Название окна
font = pygame.font.Font(None, FONT_SIZE)


class GoBoard:
    # Переменные для очков
    black_score = 0
    white_score = 0
    pass_count = 0  # Количество подряд идущих пасов
    game_over = False

    def __init__(self, size=BOARD_SIZE):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]  # Инициализация доски
        self.current_player = 'X'  # Начинает игрок 'X'

    def is_within_bounds(self, row, col):
        """Проверка, что координаты находятся в пределах доски"""
        return 0 <= row < self.size and 0 <= col < self.size

    def place_stone(self, row, col):
        """Размещение камня на доске и проверка захвата камней противника"""
        if not self.is_within_bounds(row, col) or self.board[row][col] != '.':
            return False

        self.pass_count = 0

        # Помещение камня на доску
        self.board[row][col] = self.current_player
        # Проверка на захват камней противника
        self.check_capture(row, col)
        # Смена текущего игрока
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def pass_move(self):
        """Игрок совершает пас."""
        self.pass_count += 1
        if self.current_player == 'X':
            self.black_score += 1
        else:
            self.white_score += 1
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        if self.pass_count >= 2:  # Если два игрока пасуют подряд
            self.end_game()

    def check_capture(self, row, col):
        """Проверка и захват камней противника"""
        color = self.board[row][col]
        opponent_color = 'O' if color == 'X' else 'X'

        def get_group(row, col):
            """Получение группы связанных камней"""
            _color = self.board[row][col]
            group = set()
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                if (r, c) in group:
                    continue
                group.add((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if self.is_within_bounds(nr, nc) and self.board[nr][nc] == _color and (nr, nc) not in group:
                        stack.append((nr, nc))
            return group

        def has_liberties(group):
            """Проверка наличия свободных точек у группы"""
            for r, c in group:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if self.is_within_bounds(nr, nc) and self.board[nr][nc] == '.':
                        return True
            return False

        # Проверка захвата камней противника
        for r, c in get_group(row, col):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if self.is_within_bounds(nr, nc) and self.board[nr][nc] == opponent_color:
                    group = get_group(nr, nc)
                    if not has_liberties(group):
                        if self.current_player == 'X':
                            self.black_score += len(group)
                        else:
                            self.white_score += len(group)
                        for gr, gc in group:
                            self.board[gr][gc] = '.'  # Удаление захваченных камней

    def draw(self, surface):
        """Оптимизированная отрисовка доски, очков и камней на экране"""
        surface.fill(BACKGROUND_COLOR)  # Установка фона

        half_grid = GRID_SIZE // 2
        window_end = WINDOW_WIDTH - half_grid

        self.draw_lines(half_grid, surface, window_end)
        self.draw_stones(half_grid, surface)
        self.draw_scores(half_grid, surface)
        self.draw_buttons(half_grid, surface)

    def draw_lines(self, half_grid, surface, window_end):
        """Рисование линий"""
        for i in range(self.size):
            pos = half_grid + i * GRID_SIZE
            pygame.draw.line(surface, LINE_COLOR, (half_grid, pos), (window_end, pos), LINE_WIDTH)
            pygame.draw.line(surface, LINE_COLOR, (pos, half_grid), (pos, window_end), LINE_WIDTH)

    def draw_scores(self, half_grid, surface):
        """Рисование очков"""
        black_text = font.render(f'Черные: {self.black_score}', True, TEXT_COLOR)
        surface.blit(black_text, (half_grid, WINDOW_HEIGHT - FONT_SIZE))
        white_text = font.render(f'Белые: {self.white_score}', True, TEXT_COLOR)
        surface.blit(white_text, (half_grid, WINDOW_HEIGHT - 2 * FONT_SIZE))

    def draw_stones(self, half_grid, surface):
        """Рисование камней"""
        for (row, col) in product(range(BOARD_SIZE), repeat=2):
            color = self.board[row][col]
            if color == ".":  # Проверяем только если есть камень
                continue
            stone_color = BLACK_STONE_COLOR if color == 'X' else WHITE_STONE_COLOR
            pygame.draw.circle(
                surface, stone_color,
                (half_grid + col * GRID_SIZE, half_grid + row * GRID_SIZE),
                STONE_RADIUS
            )

    def draw_buttons(self, half_grid, surface):
        """Отрисовка кнопок"""
        rect = pygame.Rect(WINDOW_WIDTH - 100 - half_grid, WINDOW_HEIGHT - 40 - half_grid, 100, 40)
        pygame.draw.rect(surface, BUTTON_COLOR, rect)  # Рисуем прямоугольник кнопки
        text_surface = font.render("Пас", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)  # Отображаем текст по центру кнопки

    def end_game(self):
        """Завершение игры и подсчет очков."""
        self.game_over = True
        print("Игра закончена. Подсчет очков...")


def main():
    """Основная функция для запуска игры"""
    board = GoBoard()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // GRID_SIZE
                col = x // GRID_SIZE
                if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                    board.place_stone(row, col)

                if pass_button_rect.collidepoint(event.pos):
                    board.pass_move()

        if board.game_over:
            pygame.quit()
            sys.exit()

        board.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()

from loging import game_logger
from config import *
from score_counter import count_chinese_score


class GoGameLogic:
    # Переменные для очков
    black_score = 0
    white_score = 0
    pass_count = 0  # Количество подряд идущих пасов
    game_over = False

    def __init__(self, size, bord_config: BoardConfig, board=None, fake=False):
        self.size = size
        self.fake = fake
        self.bordConfig = bord_config
        # Инициализация доски
        self.board = [['.' for _ in range(size)] for _ in range(size)] \
            if board is None else board
        self.current_player = 'B'  # Начинает игрок 'B'

    def is_in_bounds(self, row, col):
        """Проверка, что координаты находятся в пределах доски"""
        return 0 <= row < self.size and 0 <= col < self.size

    def place_stone(self, row, col):
        """Размещение камня на доске и проверка захвата камней противника"""
        if not self.is_in_bounds(row, col) or self.board[row][col] != '.':
            return False

        if not self.fake:
            game_logger.info(f"{self.current_player}: ({row}, {col})")
        self.pass_count = 0

        # Помещение камня на доску
        self.board[row][col] = self.current_player
        # Проверка на захват камней противника
        self.check_capture(row, col, self.current_player)
        # Смена текущего игрока
        self.current_player = 'W' if self.current_player == 'B' else 'B'
        self.check_capture(row, col, self.current_player)
        return True

    def pass_move(self):
        """Игрок совершает пас."""
        self.pass_count += 1
        if self.current_player == 'B':
            self.black_score += 1
        else:
            self.white_score += 1
        self.current_player = 'W' if self.current_player == 'B' else 'B'
        if self.pass_count >= 2:
            self.end_game()

    def check_capture(self, row, col, opponent_color):
        """Проверка и захват камней противника"""

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
                    if self.is_in_bounds(nr, nc) and self.board[nr][nc] == _color and (nr, nc) not in group:
                        stack.append((nr, nc))
            return group

        def has_liberties(group):
            """Проверка наличия свободных точек у группы"""
            for r, c in group:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if self.is_in_bounds(nr, nc) and self.board[nr][nc] == '.':
                        return True
            return False

        is_delite = False

        # Проверка захвата камней противника
        for r, c in get_group(row, col):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if self.is_in_bounds(nr, nc) and self.board[nr][nc] == opponent_color:
                    group = get_group(nr, nc)
                    if not has_liberties(group):
                        is_delite = True
                        if self.current_player == 'B':
                            self.black_score += len(group)
                        else:
                            self.white_score += len(group)
                        for gr, gc in group:
                            self.board[gr][gc] = '.'  # Удаление захваченных камней

        if is_delite:
            return
        # Самострел
        group = get_group(row, col)
        if not has_liberties(group):
            for gr, gc in group:
                self.board[gr][gc] = '.'  # Удаление захваченных камней

    def end_game(self):
        """Завершение игры и подсчет очков."""
        self.game_over = True
        print("Игра закончена. Подсчет очков...")
        print(count_chinese_score(self.board))


class GoGameGUI:
    def __init__(self, game_logic, surface):
        self.game_logic = game_logic
        self.surface = surface
        self.bordConfig = game_logic.bordConfig

    def draw(self):
        """Метод для отрисовки всего"""
        self.surface.fill(BACKGROUND_COLOR)  # Установка фона

        half_grid = self.bordConfig.GRID_SIZE() // 2
        window_end = WINDOW_WIDTH - half_grid

        self.draw_lines(half_grid, window_end)
        self.draw_stones(half_grid)
        self.draw_scores(half_grid)
        self.draw_buttons(half_grid)

    def draw_lines(self, half_grid, window_end):
        """Рисование линий"""
        for i in range(self.game_logic.size):
            pos = half_grid + i * self.bordConfig.GRID_SIZE()
            pygame.draw.line(self.surface, LINE_COLOR, (half_grid, pos), (window_end, pos), LINE_WIDTH)
            pygame.draw.line(self.surface, LINE_COLOR, (pos, half_grid), (pos, window_end), LINE_WIDTH)

    def draw_scores(self, half_grid):
        font = pygame.font.Font(None, FONT_SIZE)
        """Рисование очков"""
        black_text = font.render(f'Черные: {self.game_logic.black_score}', True, TEXT_COLOR)
        self.surface.blit(black_text, (half_grid, WINDOW_HEIGHT - FONT_SIZE))
        white_text = font.render(f'Белые: {self.game_logic.white_score}', True, TEXT_COLOR)
        self.surface.blit(white_text, (half_grid, WINDOW_HEIGHT - 2 * FONT_SIZE))

    def draw_stones(self, half_grid):
        """Рисование камней"""
        for row in range(self.game_logic.size):
            for col in range(self.game_logic.size):
                color = self.game_logic.board[row][col]
                if color == ".":  # Проверяем только если есть камень
                    continue
                stone_color = BLACK_STONE_COLOR if color == 'B' else WHITE_STONE_COLOR
                pygame.draw.circle(
                    self.surface, stone_color,
                    (half_grid + col * self.bordConfig.GRID_SIZE(), half_grid + row * self.bordConfig.GRID_SIZE()),
                    self.bordConfig.STONE_RADIUS()
                )

    def draw_buttons(self, half_grid):
        font = pygame.font.Font(None, FONT_SIZE)
        """Отрисовка кнопок"""
        rect = pygame.Rect(WINDOW_WIDTH - 100 - half_grid, WINDOW_HEIGHT - 40 - half_grid, 100, 40)
        pygame.draw.rect(self.surface, BUTTON_COLOR, rect)
        text_surface = font.render("Пас", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.surface.blit(text_surface, text_rect)

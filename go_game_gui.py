import pygame
import configuration as cfg


class GoGameGUI:
    def __init__(self, game_logic, surface):
        self.show_help = False
        self.game_logic = game_logic
        self.surface = surface
        self.bordConfig = game_logic.bordConfig

    def draw(self):
        """Метод для отрисовки всего"""
        self.surface.fill(cfg.BACKGROUND_COLOR)  # Установка фона
        grid_cell = self.bordConfig.GRID_CELL_SIZE()
        half_grid_cell = self.bordConfig.GRID_CELL_SIZE() // 2
        window_end = cfg.WINDOW_WIDTH - half_grid_cell

        self.draw_lines(half_grid_cell, window_end)
        self.draw_stones(half_grid_cell)
        self.draw_scores(grid_cell)
        self.draw_buttons(grid_cell)

        if self.show_help:
            self.draw_help()

    def draw_lines(self, half_grid, window_end):
        """Рисование линий"""
        board_size = self.bordConfig.BOARD_SIZE
        for i in range(board_size):
            pos = half_grid + i * self.bordConfig.GRID_CELL_SIZE()

            # Ограничиваем линию по ширине
            start_x = half_grid
            end_x = min(window_end,
                        half_grid + (board_size - 1) * self.bordConfig.GRID_CELL_SIZE())

            pygame.draw.line(self.surface, cfg.LINE_COLOR, (start_x, pos), (end_x, pos), cfg.LINE_WIDTH)

            # Ограничиваем линию по высоте
            start_y = half_grid
            end_y = min(window_end,
                        half_grid + (board_size - 1) * self.bordConfig.GRID_CELL_SIZE())

            pygame.draw.line(self.surface, cfg.LINE_COLOR, (pos, start_y), (pos, end_y), cfg.LINE_WIDTH)

    def draw_scores(self, grid_cell):
        font = pygame.font.Font(None, cfg.FONT_SIZE)
        """Рисование очков"""
        board_size = self.bordConfig.BOARD_SIZE
        black_text = font.render(f'Черные: {self.game_logic.black_score}', True, cfg.TEXT_COLOR)
        self.surface.blit(black_text, (25, max(grid_cell * board_size, cfg.WINDOW_HEIGHT - 50 - 25 - 50)))
        white_text = font.render(f'Белые: {self.game_logic.white_score}', True, cfg.TEXT_COLOR)
        self.surface.blit(white_text, (25, max(grid_cell * board_size + cfg.FONT_SIZE,
                                               cfg.WINDOW_HEIGHT - 50 - 25 - 50 + cfg.FONT_SIZE)))

    def draw_stones(self, half_grid):
        """Рисование камней"""
        board_size = self.bordConfig.BOARD_SIZE
        for row in range(board_size):
            for col in range(board_size):
                color = self.game_logic.board[row][col]
                if color == ".":  # Проверяем только если есть камень
                    continue
                stone_color = cfg.BLACK_STONE_COLOR if color == 'B' else cfg.WHITE_STONE_COLOR
                pygame.draw.circle(
                    self.surface, stone_color,
                    (half_grid + col * self.bordConfig.GRID_CELL_SIZE(),
                     half_grid + row * self.bordConfig.GRID_CELL_SIZE()),
                    self.bordConfig.STONE_RADIUS()
                )

    def draw_buttons(self, grid_cell):
        font = pygame.font.Font(None, cfg.FONT_SIZE)
        board_size = self.bordConfig.BOARD_SIZE
        """Отрисовка кнопок"""
        rect = pygame.Rect(cfg.WINDOW_WIDTH // 2 - 50,
                           max(grid_cell * board_size, cfg.WINDOW_HEIGHT - 50 - 25 - 50),
                           50 * 2, 50)
        pygame.draw.rect(self.surface, cfg.BUTTON_COLOR, rect)
        text_surface = font.render("Пас", True, cfg.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.surface.blit(text_surface, text_rect)

        rect = pygame.Rect(cfg.WINDOW_WIDTH - 25 - 50,
                           max(grid_cell * board_size, cfg.WINDOW_HEIGHT - 50 - 25 - 50),
                           50, 50)
        pygame.draw.rect(self.surface, cfg.BUTTON_COLOR, rect)
        text_surface = font.render("?", True, cfg.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.surface.blit(text_surface, text_rect)

    def draw_help(self):
        font = pygame.font.Font(None, 25)
        font.set_underline(True)
        rect = pygame.Rect(0, cfg.WINDOW_HEIGHT - 50, cfg.WINDOW_WIDTH, 25)
        pygame.draw.rect(self.surface, cfg.BUTTON_COLOR, rect)
        text_surface = font.render("Правила игры", True, cfg.LINK_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.surface.blit(text_surface, text_rect)

        font = pygame.font.Font(None, 18)
        rect = pygame.Rect(0, cfg.WINDOW_HEIGHT - 25, cfg.WINDOW_WIDTH, 25)
        pygame.draw.rect(self.surface, cfg.BUTTON_COLOR, rect)
        text_surface = font.render("P. S.: Для завершения игры два игрока должны спасовать", True, cfg.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.surface.blit(text_surface, text_rect)

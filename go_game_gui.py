import pygame
import configuration as cfg


class GoGameGUI:
    def __init__(self, game_logic, surface):
        self.game_logic = game_logic
        self.surface = surface
        self.bordConfig = game_logic.bordConfig

    def draw(self):
        """Метод для отрисовки всего"""
        self.surface.fill(cfg.BACKGROUND_COLOR)  # Установка фона

        half_grid = self.bordConfig.GRID_SIZE() // 2
        window_end = cfg.WINDOW_WIDTH - half_grid

        self.draw_lines(half_grid, window_end)
        self.draw_stones(half_grid)
        self.draw_scores(half_grid)
        self.draw_buttons(half_grid)

    def draw_lines(self, half_grid, window_end):
        """Рисование линий"""
        for i in range(self.game_logic.size):
            pos = half_grid + i * self.bordConfig.GRID_SIZE()
            pygame.draw.line(self.surface, cfg.LINE_COLOR, (half_grid, pos), (window_end, pos), cfg.LINE_WIDTH)
            pygame.draw.line(self.surface, cfg.LINE_COLOR, (pos, half_grid), (pos, window_end), cfg.LINE_WIDTH)

    def draw_scores(self, half_grid):
        font = pygame.font.Font(None, cfg.FONT_SIZE)
        """Рисование очков"""
        black_text = font.render(f'Черные: {self.game_logic.black_score}', True, cfg.TEXT_COLOR)
        self.surface.blit(black_text, (half_grid, cfg.WINDOW_HEIGHT - cfg.FONT_SIZE))
        white_text = font.render(f'Белые: {self.game_logic.white_score}', True, cfg.TEXT_COLOR)
        self.surface.blit(white_text, (half_grid, cfg.WINDOW_HEIGHT - 2 * cfg.FONT_SIZE))

    def draw_stones(self, half_grid):
        """Рисование камней"""
        for row in range(self.game_logic.size):
            for col in range(self.game_logic.size):
                color = self.game_logic.board[row][col]
                if color == ".":  # Проверяем только если есть камень
                    continue
                stone_color = cfg.BLACK_STONE_COLOR if color == 'B' else cfg.WHITE_STONE_COLOR
                pygame.draw.circle(
                    self.surface, stone_color,
                    (half_grid + col * self.bordConfig.GRID_SIZE(), half_grid + row * self.bordConfig.GRID_SIZE()),
                    self.bordConfig.STONE_RADIUS()
                )

    def draw_buttons(self, half_grid):
        font = pygame.font.Font(None, cfg.FONT_SIZE)
        """Отрисовка кнопок"""
        rect = pygame.Rect(cfg.WINDOW_WIDTH - 100 - half_grid, cfg.WINDOW_HEIGHT - 40 - half_grid, 100, 40)
        pygame.draw.rect(self.surface, cfg.BUTTON_COLOR, rect)
        text_surface = font.render("Пас", True, cfg.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.surface.blit(text_surface, text_rect)

# импорты
import pygame

# Настройки
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 500


class BoardConfig:
    def __init__(self):
        self.BOARD_SIZE = 9

    def GRID_SIZE(self):
        return WINDOW_WIDTH // self.BOARD_SIZE

    def STONE_RADIUS(self):
        return self.GRID_SIZE() // 3  # Радиус камня


LINE_WIDTH = 2  # Толщина линий сетки
STONE_WIDTH = 15  # Толщина камня
FONT_SIZE = 32

# Цвета

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BACKGROUND_COLOR = (222, 184, 135)  # Цвет фона
LINE_COLOR = BLACK  # Цвет линий сетки
TEXT_COLOR = BLACK
BUTTON_COLOR = (128, 128, 128)
BLACK_STONE_COLOR = BLACK  # Цвет черного камня
WHITE_STONE_COLOR = WHITE  # Цвет белого камня
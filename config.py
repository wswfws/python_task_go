# Настройки
import pygame

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 500
BOARD_SIZE = 9
GRID_SIZE = WINDOW_WIDTH // BOARD_SIZE
LINE_WIDTH = 2  # Толщина линий сетки
STONE_RADIUS = GRID_SIZE // 3  # Радиус камня
STONE_WIDTH = 15  # Толщина камня
FONT_SIZE = 32

# Цвета
BACKGROUND_COLOR = (222, 184, 135)  # Цвет фона
LINE_COLOR = (0, 0, 0)  # Цвет линий сетки
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (128, 128, 128)
BLACK_STONE_COLOR = (0, 0, 0)  # Цвет черного камня
WHITE_STONE_COLOR = (255, 255, 255)  # Цвет белого камня

pass_button_rect = pygame.Rect(WINDOW_WIDTH - 100 - GRID_SIZE // 2, WINDOW_HEIGHT - 40 - GRID_SIZE // 2, 100, 40)

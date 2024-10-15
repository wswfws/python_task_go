# Настройки
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 570

sessionid = "" #not commit
game_id = 68664722


class BoardConfig:
    def __init__(self):
        self.BOARD_SIZE = 9

    def GRID_CELL_SIZE(self):
        return WINDOW_WIDTH // self.BOARD_SIZE

    def STONE_RADIUS(self):
        return self.GRID_CELL_SIZE() // 3  # Радиус камня


LINE_WIDTH = 2  # Толщина линий сетки
STONE_WIDTH = 15  # Толщина камня
FONT_SIZE = 32
FONT_SIZE_END = 50

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
LINK_COLOR = (5, 58, 145)

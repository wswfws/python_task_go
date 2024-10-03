import sys
import pygame
import configuration as cfg

from go_game_logic import GoGameLogic
from go_game_gui import GoGameGUI
from bot import get_deep_move
from menu import show_menu, Settings

global BOARD_SIZE

bordConfig = cfg.BoardConfig()

# Инициализация pygame
pygame.init()
screen = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT))  # Создание окна
pygame.display.set_caption("Go Game")  # Название окна

pass_button_rect = pygame.Rect(
    cfg.WINDOW_WIDTH - 100 - bordConfig.GRID_SIZE() // 2,
    cfg.WINDOW_HEIGHT - 40 - bordConfig.GRID_SIZE() // 2,
    100, 40
)


def main(_settings: Settings):
    """
    Основная функция для запуска игры"""
    board_logic = GoGameLogic(_settings.bord_size, bordConfig)
    board_gui = GoGameGUI(board_logic, screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // bordConfig.GRID_SIZE()
                col = x // bordConfig.GRID_SIZE()
                if 0 <= row < _settings.bord_size and 0 <= col < _settings.bord_size:
                    if board_logic.place_stone(row, col) and _settings.state == "single":
                        board_logic.place_stone(*get_deep_move(board_logic.board, board_logic.current_player))

                if pass_button_rect.collidepoint(event.pos):
                    board_logic.pass_move()

        if board_logic.game_over:
            pygame.quit()
            sys.exit()

        board_gui.draw()
        pygame.display.flip()


if __name__ == "__main__":
    settings = show_menu()
    bordConfig.BOARD_SIZE = settings.bord_size
    if settings.state == "exit":
        exit()
    main(settings)

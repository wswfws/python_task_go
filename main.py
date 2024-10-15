import sys
import webbrowser
import pygame
import configuration as cfg

from go_game_logic import GoGameLogic
from go_game_gui import GoGameGUI
from bot import bots
from menu_window import show_menu, Settings
from game_over_window import show_end

bordConfig = cfg.BoardConfig()

# Инициализация pygame
pygame.init()
screen = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT))  # Создание окна
pygame.display.set_caption("Go Game")  # Название окна

pass_button_rect = pygame.Rect(
    cfg.WINDOW_WIDTH // 2 - 50,
    max(bordConfig.GRID_CELL_SIZE() * bordConfig.BOARD_SIZE, cfg.WINDOW_HEIGHT - 50 - 25 - 50),
    50 * 2, 50
)

question_button_rect = pygame.Rect(
    cfg.WINDOW_WIDTH - 25 - 50,
    max(bordConfig.GRID_CELL_SIZE() * bordConfig.BOARD_SIZE, cfg.WINDOW_HEIGHT - 50 - 25 - 50),
    50, 50
)

game_rules_rect = pygame.Rect(0, cfg.WINDOW_HEIGHT - 50, cfg.WINDOW_WIDTH, 25)


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
                row = y // bordConfig.GRID_CELL_SIZE()
                col = x // bordConfig.GRID_CELL_SIZE()
                if 0 <= row < _settings.bord_size and 0 <= col < _settings.bord_size:
                    normal_move = board_logic.place_stone(row, col)
                    if normal_move and _settings.state == "single":
                        board_logic.place_stone(
                            *bots[_settings.bot_hard](board_logic.board, board_logic.current_player))
                    if normal_move and _settings.state == "online":
                        pass

                if pass_button_rect.collidepoint(event.pos):
                    board_logic.pass_move()

                if question_button_rect.collidepoint(event.pos):
                    board_gui.show_help = True
                    pygame.display.flip()

                if game_rules_rect.collidepoint(event.pos) and board_gui.show_help:
                    webbrowser.open("https://ufgo.org/Rules9x9/Go%20Rules%209x9.htm")

        if board_logic.game_over:
            show_end(board_logic.black_score, board_logic.white_score)
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

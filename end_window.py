import pygame
import configuration as cfg


class End:
    def __init__(self, black_score, white_score):
        pygame.init()
        self.black_score = black_score
        self.white_score = white_score
        self.screen = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT))  # Создание окна
        pygame.display.set_caption("Game over")  # Название окна
        self.font = pygame.font.Font(None, cfg.FONT_SIZE_END)

        self.game_over_rect = pygame.Rect(50, 50, 350, 100)
        self.winner_rect = pygame.Rect(50, 350, 350, 100)
        self.circle_black = pygame.Rect(62.5, 200, 100, 100)
        self.circle_white = pygame.Rect(287.5, 200, 100, 100)

    def draw(self):
        """Оптимизированная отрисовка доски, очков и камней на экране"""
        self.screen.fill(cfg.BACKGROUND_COLOR)  # Установка фона
        self.draw_buttons()

    def draw_buttons(self):
        """Отрисовка кнопок"""
        # ПРЯМОУГОЛЬНИК "ИГРА ОКОНЧЕНА!"
        pygame.draw.rect(self.screen, cfg.BUTTON_COLOR, self.game_over_rect)  # Рисуем прямоугольник кнопки
        text_surface = self.font.render("Игра окончена!", True, cfg.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.game_over_rect.center)
        self.screen.blit(text_surface, text_rect)  # Отображаем текст по центру кнопки

        # СЧЁТ ЧЕРНЫХ
        pygame.draw.circle(self.screen, cfg.BLACK_STONE_COLOR, (cfg.WINDOW_WIDTH/4, 250), 50)
        text_surface = self.font.render(f'{self.black_score}', True, cfg.WHITE)
        text_rect = text_surface.get_rect(center=self.circle_black.center)
        self.screen.blit(text_surface, text_rect)

        # СЧЁТ БЕЛЫХ
        pygame.draw.circle(self.screen, cfg.WHITE_STONE_COLOR, (cfg.WINDOW_WIDTH - cfg.WINDOW_WIDTH/4, 250), 50)
        text_surface = self.font.render(f'{self.white_score}', True, cfg.BLACK)
        text_rect = text_surface.get_rect(center=self.circle_white.center)
        self.screen.blit(text_surface, text_rect)

        # ДВОЕТОЧИЕ
        pygame.draw.circle(self.screen, cfg.BLACK, (cfg.WINDOW_WIDTH/2, 235), 2)
        pygame.draw.circle(self.screen, cfg.BLACK, (cfg.WINDOW_WIDTH/2, 265), 2)

        # ПРЯМОУГОЛЬНИК "ПОБЕДА <player>"
        pygame.draw.rect(self.screen, cfg.BUTTON_COLOR, self.winner_rect)  # Рисуем прямоугольник
        if self.white_score < self.black_score:
            text_surface = self.font.render("Победа чёрных", True, cfg.TEXT_COLOR)
        elif self.white_score > self.black_score:
            text_surface = self.font.render("Победа белых", True, cfg.TEXT_COLOR)
        else:
            text_surface = self.font.render("Ничья", True, cfg.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.winner_rect.center)
        self.screen.blit(text_surface, text_rect)  # Отображаем текст по центру кнопки


def show_end(black_score, white_score):
    end = End(black_score, white_score)

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        end.draw()
        pygame.display.flip()


if __name__ == "__main__":
    show_end(5, 5)

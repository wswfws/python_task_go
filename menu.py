import pygame
from dataclasses import dataclass
from input_box import InputBox
from configuration import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FONT_SIZE,
    BUTTON_COLOR,
    TEXT_COLOR,
    BACKGROUND_COLOR,
    RED)

start_button_rect_single = pygame.Rect(10, 10, 200, 40)
start_button_rect_multi = pygame.Rect(10, 60, 200, 40)
start_button_rect_exit = pygame.Rect(10, 110, 200, 40)


class StartMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Создание окна
        pygame.display.set_caption("Go Game menu")  # Название окна
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.get_bord_size_input = InputBox(10, 210, 100, 40, "9")

    def draw(self):
        """Оптимизированная отрисовка доски, очков и камней на экране"""
        self.screen.fill(BACKGROUND_COLOR)  # Установка фона

        self.draw_buttons()
        self.draw_settings()

    def handle_event(self, event):
        self.get_bord_size_input.handle_event(event)

    def get_bord_size(self):
        return self.get_bord_size_input.text

    def draw_settings(self):
        black_text = self.font.render(f'Размер Поля', True, TEXT_COLOR)
        self.screen.blit(black_text, (10, 160))
        self.get_bord_size_input.draw(self.screen)

    def draw_buttons(self):
        """Отрисовка кнопок"""
        pygame.draw.rect(self.screen, BUTTON_COLOR, start_button_rect_single)  # Рисуем прямоугольник кнопки
        text_surface = self.font.render("Против бота", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=start_button_rect_single.center)
        self.screen.blit(text_surface, text_rect)  # Отображаем текст по центру кнопки

        pygame.draw.rect(self.screen, BUTTON_COLOR, start_button_rect_multi)  # Рисуем прямоугольник кнопки
        text_surface = self.font.render("Вдвоём", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=start_button_rect_multi.center)
        self.screen.blit(text_surface, text_rect)  # Отображаем текст по центру кнопки

        pygame.draw.rect(self.screen, RED, start_button_rect_exit)  # Рисуем прямоугольник кнопки
        text_surface = self.font.render("Выйти", True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=start_button_rect_exit.center)
        self.screen.blit(text_surface, text_rect)  # Отображаем текст по центру кнопки


@dataclass
class Settings:
    state: str  # "single"|"multi"|"quit"
    bord_size: int = 9


def show_menu():
    """
    show start menu
    :return: Settings
    """

    menu = StartMenu()

    running = True
    while running:
        for event in pygame.event.get():
            menu.handle_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect_single.collidepoint(event.pos):
                    return Settings("single", int(menu.get_bord_size()))
                if start_button_rect_multi.collidepoint(event.pos):
                    return Settings("multi", int(menu.get_bord_size()))
                if start_button_rect_exit.collidepoint(event.pos):
                    return Settings("exit", int(menu.get_bord_size()))

        menu.draw()
        pygame.display.flip()

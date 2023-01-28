import pygame

import sys


class Minion:
    """Класс для персонажа"""

    def __init__(self, screen):
        """Инициализирует персонажа и задает его начальную позицию"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #  Загружает изображение персонажа и получает прямоугольник
        self.image = pygame.image.load('images/task2.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует персонажа в текущей позиции"""
        self.screen.blit(self.image, self.rect)


class Start:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Minion")
        self.minion = Minion(self.screen)

    def run_game(self):
        """Запуск основного центра игры"""
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill((255, 255, 255))
        self.minion.blitme()

        # Отображение последнего прорисованого экрана
        pygame.display.flip()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    start = Start()
    start.run_game()

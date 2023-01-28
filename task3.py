import pygame

import sys


class Start:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")
        self.rocket = Rocket(self)

    def run_game(self):
        """Запуск основного центра игры"""
        while True:
            self._check_events()
            self.rocket.update()
            self.screen.fill((255, 255, 255))
            self.rocket.blitme()
            pygame.display.flip()

        # Отображение последнего прорисованого экрана

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_event(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False


class Rocket():
    """Класс для персонажа"""

    def __init__(self, ai_game):
        """Инициализирует персонажа и задает его начальную позицию"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #  Загружает изображение персонажа и получает прямоугольник
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # Сохранение вещественной координаты центра ракеты
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию ракеты с учетом флага"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        if self.moving_up and self.rect.top > 0:
            self.y -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует персонажа в текущей позиции"""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    start = Start()
    start.run_game()

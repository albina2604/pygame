import pygame
from pygame.sprite import Sprite
import sys
from time import sleep


class Start:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain")
        self.fleet_drop_speed = 10
        self.moving_down = True
        self.stars = pygame.sprite.Group()
        self.create_fleet()

    def create_fleet(self):
        """Создание флота пришельцев"""
        # Создание пришельца и расчет количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width
        number_aliens_x = available_space_x // star_width

        # Определение количества рядов

        available_space_y = self.screen_height
        number_rows = available_space_y // star_height

        # Создание флота пришельцев
        for row_number in range(number_rows):
            for star_number in range(number_aliens_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        # Создание звезды и расположение его в ряду
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * row_number
        self.stars.add(star)

    def _check_star_bottom(self):
        for star in self.stars.sprites():
            if self.moving_down == True:
                self._star_drop()
                break

    def _star_drop(self):
        screen_rect = self.screen.get_rect()
        for star in self.stars.sprites():
            if not star.rect.bottom >= screen_rect.bottom:
                star.rect.y += self.fleet_drop_speed
            else:
                star.kill()

    def run_game(self):
        """Запуск основного центра игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update_stars()
            self._update_screen()

    def update_stars(self):
        self._check_star_bottom()
        self._star_drop()
        self.stars.update()
        sleep(0.2)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill((255, 255, 255))
        self.stars.draw(self.screen)
        # Отображение последнего прорисованого экрана
        pygame.display.flip()


class Star(Sprite):
    """Класс для звезды"""

    def __init__(self, start_game):
        """Инициализирует звезду и задает его начальную позицию"""
        super().__init__()
        self.screen = start_game.screen

        # Загрузка рисунка пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/drop.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца
        self.y = float(self.rect.y)


if __name__ == '__main__':
    start = Start()
    start.run_game()

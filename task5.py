import pygame
import sys
from pygame.sprite import Sprite


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Stars")
        self.bg_color = (255, 255, 255)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного центра игры"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            pygame.display.flip()

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
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.left <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Отображение последнего прорисованого экрана
        pygame.display.flip()


class Ship():
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.ship_speed = 1.5
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #  Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midleft = self.screen_rect.midleft

        # Сохранение вещественной координаты центра корабля
        self.y = float(self.rect.y)

        # Флаг перемещения
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию ракеты с учетом флага"""

        if self.moving_up and self.rect.top > 0:
            self.y -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5

        self.rect.y = self.y

    def blitme(self):
        """Рисует персонажа в текущей позиции"""
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем"""

    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen

        self.bullet_speed = 1.5
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(
            0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        # Позиция снаряда хранится в вещественном формате
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

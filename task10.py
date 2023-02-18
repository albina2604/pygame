import sys
import pygame
import random


class Ball:
    def __init__(self, catcher_game, x=None, y=None):
        self.screen = catcher_game.screen
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        if x:
            self.rect.x = x
            self.rect.y = y
        else:
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
        # збереження точної горизонтальної позиції
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y += 1
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Catcher:
    def __init__(self, catcher_game):
        self.screen = catcher_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/human.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # збереження точної горизонтальної позиції
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 3
        if self.moving_left and self.rect.left > 0:
            self.x -= 3
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.catcher = Catcher(catcher_game=self)
        self.ball = Ball(x=random.randint(10, self.screen_width-10),
                         y=random.randint(0, self.screen_height-200), catcher_game=self)
        self.catcher.rect.bottom = self.screen.get_rect().bottom
        self.loses = 0
        self.game = True

    def run_game(self):
        while True:
            if self.game:
                self._check_ball()
                self._check_events()
                self._update_catcher()
            self._check_events()
            self._update_screen()

    def _update_catcher(self):
        self.catcher.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.catcher.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.catcher.moving_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.catcher.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.catcher.moving_left = False

    def _check_ball(self):
        if (self.catcher.rect.top <= self.ball.rect.bottom < self.catcher.rect.bottom and (self.catcher.rect.left < self.ball.rect.left < self.catcher.rect.right or self.catcher.rect.left < self.ball.rect.right < self.catcher.rect.right)):
            self.ball = Ball(x=random.randint(0, self.screen_width), y=random.randint(
                0, self.screen_height-200), catcher_game=self)
        elif self.ball.rect.bottom == self.screen_height:
            self.ball = Ball(x=random.randint(0, self.screen_width), y=random.randint(
                0, self.screen_height-200), catcher_game=self)
        else:
            self.ball.update()

    def _update_screen(self):
        self.screen.fill((255, 255, 255))
        self.catcher.blitme()
        self.ball.blitme()

        pygame.display.flip()


game = Game()
game.run_game()

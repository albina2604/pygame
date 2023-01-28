import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Blue Sky")
while True:
    screen.fill((0, 0, 255))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

import pygame
import sys


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def check_keydown_events(event):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    else:
        print(event.key)


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Task 4")

while True:
    check_events()
    pygame.display.flip()

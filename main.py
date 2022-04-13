import pygame
from GameWindow import GameWindow
from Navigation import Navigation
from StartWindow import *
from constants import *

surface=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Snake Gesture")

clock=pygame.time.Clock()

start_window=StartWindow()
game_window= GameWindow(BLUE)
navigator= Navigation()

run=True

while run:

    clock.tick(FPS)

    events=pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run=False

    navigator.render(surface)
    # start_window.render(surface)
    pygame.display.update()

pygame.quit


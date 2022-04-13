import pygame
from GameWindow import GameWindow
from StartWindow import *
from constants import *

win=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Snake Gesture")

clock=pygame.time.Clock()

start_window=StartWindow()
game_window= GameWindow(PERSIAN_BLUE)

run=True

while run:

    clock.tick(FPS)

    events=pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run=False

    start_window.render(win)
    pygame.display.update()

pygame.quit


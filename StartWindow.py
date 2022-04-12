import os
from constants import *
import pygame
from Button import Button

class StartWindow(object):
    def __init__(self):

        self.background= pygame.image.load(os.path.join( "images","background.png"))

        self.start_button= Button(500,100,BUTTON_WIDTH,BUTTON_HEIGHT,WHITE,BLACK,TEXT_SIZE,"Start")
        self.quit_button= Button(500,200,BUTTON_WIDTH,BUTTON_HEIGHT,WHITE,BLACK,TEXT_SIZE,"Quit")


    def draw_window(self,win):
        win.blit(self.background,(0, 0))
        self.start_button.button_draw(win)
        self.quit_button.button_draw(win)

    def render(self,win):
        self.draw_window(win)
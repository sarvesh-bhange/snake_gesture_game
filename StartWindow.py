import os
from constants import *
import pygame
from Button import Button

class StartWindow(object):
    def __init__(self):

        self.start_button= Button(500,100,BUTTON_WIDTH,BUTTON_HEIGHT,BLACK,WHITE,TEXT_SIZE,"Start")
        self.quit_button= Button(500,200,BUTTON_WIDTH,BUTTON_HEIGHT,BLACK,WHITE,TEXT_SIZE,"Quit")


    def draw_window(self,surface):
        surface.fill(BLUE)
        self.start_button.button_draw(surface)
        self.quit_button.button_draw(surface)

    def render(self,surface, props, navigate,events):
        if self.start_button.isclick(events):
            navigate("GameWindow")

        if self.quit_button.isclick(events):
            pygame.quit()

        self.draw_window(surface)
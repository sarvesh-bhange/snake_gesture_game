import pygame
import os
from Button import Button
from constants import *

class GameWindow(object):
    def __init__(self,color):

        self.color=color

        self.back_button= Button(10,10,BUTTON_WIDTH,30,BLACK,WHITE,30,"Back")

        self.reset_button= Button(800,10,BUTTON_WIDTH,30,BLACK,WHITE,30,"Reset")

        self.timmer_symbol= pygame.transform.scale(pygame.image.load(os.path.join("images","timmer_symbol.png")),(30,30))

    def grid_draw(self,surface,rows,color,screen_width):

        gap_size= screen_width//rows

        x=0
        y=HEADER_HEIGHT + BORDER_HEIGHT

        for i in range(rows):

            x+=gap_size
            y+=gap_size

            pygame.draw.line(surface,color,(x,HEADER_HEIGHT + BORDER_HEIGHT),(x,527)) #vertical line
            pygame.draw.line(surface,color,(0,y),(screen_width,y)) #horizontel line    

    def draw_window(self,surface):

        surface.fill(self.color)

        self.grid_draw(surface,ROWS,WHITE,WIDTH)

        top_border= pygame.Rect(0,HEADER_HEIGHT,WIDTH,BORDER_HEIGHT)

        bottom_border= pygame.Rect(0,527,WIDTH,BORDER_HEIGHT)

        pygame.draw.rect(surface,BLACK,top_border)

        pygame.draw.rect(surface,BLACK,bottom_border)

        self.back_button.button_draw(surface)

        self.reset_button.button_draw(surface)

        surface.blit(self.timmer_symbol,(400,10))

    def render(self,surface,props,navigate,events):

        if self.back_button.isclick(events):
            navigate("StartWindow")

        if self.reset_button.isclick(events):
            pass

        self.draw_window(surface)
        

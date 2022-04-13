import pygame
from constants import *

class GameWindow(object):
    def __init__(self,color):

        self.color=color


    def grid_draw(self,surface,rows,color,screen_width):

        gap_size= screen_width//rows

        x=0
        y=0

        for i in range(rows):

            x= x+gap_size
            y= y+ gap_size

            pygame.draw.line(surface,color,(x,0),(x,screen_width))
            pygame.draw.line(surface,color,(0,y),(screen_width,y))


    

    def draw_window(self,surface):

        surface.fill(self.color)

        self.grid_draw(surface,ROWS,WHITE,WIDTH)

    def render(self,surface,props,navigate):
        self.draw_window(surface)
        

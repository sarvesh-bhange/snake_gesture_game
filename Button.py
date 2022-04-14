import pygame
pygame.font.init()

class Button(object):
    def __init__(self,x,y,width,height,color,buton_color,text_size,text=""):

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.button_color=buton_color
        self.text=text
        self.text_size= text_size

    def isover(self):
        pos=pygame.mouse.get_pos()

        if pos[0] >= self.x and pos[0]<= self.x+self.width:
        
            if pos[1] >= self.y and pos[1] <= self.y+self.height:
                return True


    def isclick(self,events):

        for event in events:
            if event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.isover():
                    return True

    def button_draw(self,surface):
        button_rect= pygame.Rect(self.x,self.y,self.width,self.height)

        pygame.draw.rect(surface,self.button_color,(button_rect))

        button_text= pygame.font.SysFont("comicsans",self.text_size)

        button_text_render= button_text.render(self.text,1,(self.color))

        button_text_rect= button_text_render.get_rect()

        button_center_x= self.x + self.width/2 

        button_center_y= self.y +self.height/2

        button_text_x= button_center_x - button_text_rect.width/2

        button_text_y= button_center_y - button_text_rect.height/2


        surface.blit(button_text_render,(button_text_x,button_text_y))


    def render(self,surface):
        self.button_draw(surface)
        




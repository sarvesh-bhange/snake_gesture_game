from GameWindow import GameWindow
from StartWindow import StartWindow
from constants import *


class Navigation (object):
    def __init__(self):

        self.current_window= "StartWindow"

        self.props= None

        self.windows= {"StartWindow":StartWindow(),"GameWindow":GameWindow(BLUE)}


    def render(self,surface,events):
        self.windows[self.current_window].render(surface,self.props,self.navigate,events)


    def navigate(self,destination_window,props=None):
        self.current_window= destination_window

        self.props=props
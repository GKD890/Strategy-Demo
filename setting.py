import pygame as pg

class Setting:
    """Stroing settings of the game"""
    def __init__(self):
        # Screen
        self.screen_width: int = 1200
        self.screen_height:int  = 800
        self.bg_color = (230,230,230)
        self.state = "menu"

    def changeState(self,state:int):
        match state:
            case 0:
                self.state = "menu"
            case 1:
                self.state = "start"
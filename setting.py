from tkinter import Menu
import pygame as pg
from constants import CustomizedConstant as C

class Setting:
    """Stroing settings of the game"""
    screen_width  =1200
    screen_height = 800
    screen_bg_color = C.GRAY
    def __init__(self
                ,state = "menu"):
        # Screen
        # self.screen_width = width 
        # self.screen_height = height
        # self.bg_color = bg_color
        self.state = state

    def changeState(self,state:int):
        # match needs python newer than 3.10
        match state:
            case 0:
                self.state = "menu"
            case 1:
                self.state = "start"
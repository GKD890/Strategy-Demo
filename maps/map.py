import os

import pygame as pg
from ..constants import CustomizedConstant as C

class Map:
    # constructor
    def __init__(self,
                width: int,
                height: int,
                bg_color,
                level:int):
        self.width = width
        self.height = height
        self.map_array = [[0 for x in range(self.width)] for y in range(self.height)]
        self.bg_color = bg_color
        self.level = level

    def _load_map(self):
        for x in range(0,self.width,C.GRID_REC_SIZE):
            for y in range(0, self.height, C.GRID_REC_SIZE):
                rect = pg.Rect(x, y,C.GRID_REC_SIZE,C.GRID_REC_SIZE)
        
            


        
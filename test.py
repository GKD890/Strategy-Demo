import sys
import pygame as pg

from gameFunction import GameFunction as GF
from setting import Setting
from constants import CustomizedConstant as C


   
# Inlucde main_gameloop, player, ai_player,load_map,read_status,save_status(log)
def main():
    pg.init()
    setting = Setting  
    # self.screen = pg.display.set_mode((self.setting.screen_width,self.setting.screen_height))
    global screen
    screen = pg.display.set_mode((1200,800))
    pg.display.set_caption("Strategy Demo")
    # background color
    bg_color = (179,80,80) #TODO
    screen.fill(bg_color)
    
    
    while True:
        load_map()
        # self.screen.fill(self.bg_color)
        check_events()
        
        #pg.display.flip()# continue to use new window and hide old window
        pg.display.update()

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
                sys.exit()
def load_map():
        for x in range(0,400,C.GRID_REC_SIZE):
            for y in range(0, 400, C.GRID_REC_SIZE):
                rect = pg.Rect(x, y,C.GRID_REC_SIZE,C.GRID_REC_SIZE)
                pg.draw.rect(screen, C.WHITE ,rect, 1)



            
# def _update_screen(self):
    

main()


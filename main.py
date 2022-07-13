import sys
import pygame as pg

from gameFunction import GameFunction as GF
from setting import Setting
from constants import CustomizedConstant as C

class main():
    """ Overall game class"""
    # Inlucde main_gameloop, player, ai_player,load_map,read_status,save_status(log)
    def __init__(self):
        pg.init()
        self.setting = Setting  
        self.screen = pg.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pg.display.set_caption("Strategy Demo")
        cursor = pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW)
        # background color
        self.bg_color = (C.GRAY)#TODO
        
        
    def run_game(self):
        
        while True:
            self.check_events()
            #pg.display.flip()# continue to use new window and hide old window
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Using  mouse position and game state to check which callback function to use
                cur = pg.mouse.get_pos()
                GF(cur,self.setting.state)


                
    def _update_screen(self):
        self.screen.fill(self.setting)

if __name__ == '__main__':
    game = main()
    game.run_game()

    
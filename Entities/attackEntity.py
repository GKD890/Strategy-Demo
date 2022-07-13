from datetime import datetime
from Entities.entity import Unit
from ..weapon import Weapon
import pygame as pg

# ENEMY_IMAGE = 
class Atk_Unit(Unit):
    """ Create an attack unit"""
    def __init__(self, hp, type,defen,
    group,
    damage: int,
    atk_type:int,
    atk_range: int,
    atk_frequency: float,
    skill:function = None,
    weapon:Weapon = None,
    main_instance):
        super().__init__(hp,type,defen)
        # set how to attack
        self.group = group
        if weapon != None:
            self.weapon = weapon
            self.damage = damage+ weapon.damage
        else: self.damage = damage

        self.atk_type = atk_type
        self.atk_range = atk_range
        self.atk_freq = atk_frequency
        if skill != None:
            self.skill = skill
        # load images
        self.image = pg.image.load()
        self.iniPosition = self.image.get_rect()
        self.iniPosition = 
        self.screen = ai_game.screen()
        
    
    def basic_attack(self,enemy:Unit)->int:
        if self.damage<enemy.defen:
            return 1
        else:
            return self.damage-enemy.defen
    

        
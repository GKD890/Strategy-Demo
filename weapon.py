from dataclasses import dataclass
from unicodedata import name

# @dataclass
class Weapon():

    def __init__(self,
        name:str,
        damage:int,
        speed:float, # speed * atk_freq = actual speed
        range:int,
        image:str):

        self.name = name
        self.damage = damage
        self.speed = speed
        self.range = range
        self.image = 
     
    


ranged = Weapon("range_001",4,1.3,5)
katana = Weapon("kanata_001",8,1.1,1)


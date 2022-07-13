from .attackEntity import *
from ..weapon import *


class GenEnemy:
    """Generate new enemy"""
    def __init__(self) -> None:
        pass

def newPawn(self,name:str,group:list):
    pawnA = Atk_Unit(100,name,30,"1",40,"remote",1,1,katana)
    group.append(pawnA)


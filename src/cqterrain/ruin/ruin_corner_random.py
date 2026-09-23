import cadquery as cq
import random
from numpy import arange
from . import ruin_corner

def ruin_corner_random(
        length:float = 50, 
        width:float = 50, 
        height:float = 10, 
        points:int = 7,
        debug:bool = False,
        shift:tuple[float, float, float] = (-2,4,1),
        seed:str = "test"
):
    if seed:
        random.seed(seed)
        
    modifiers = arange(shift[0],shift[1]+shift[2], shift[2])
    
    adjustments = []
    for i in range(points):
        x_mod = random.choice(modifiers)
        y_mod = random.choice(modifiers)
        adjustments.append((x_mod,y_mod))
        
    return ruin_corner(
        length = length, 
        width = width, 
        height=height,
        points = points,
        debug=debug,
        adjustments = adjustments
    )
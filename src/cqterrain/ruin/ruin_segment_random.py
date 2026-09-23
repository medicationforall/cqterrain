import cadquery as cq
from . import ruin_corner_random, ruin_rectangle_random

def ruin_segment_random(
    length:float = 75, 
    width:float = 50, 
    height:float = 10, 
    points:tuple[int,int,int] = (7,7,7),
    debug:bool = False,
    shift:tuple[float, float, float] = (-2,4,1),
    seed:str = "test"
):
    segment_length = length / 3
    
    corner_one = ruin_corner_random(
        length = segment_length, 
        width = width, 
        height = height, 
        points = points[0],
        debug = debug,
        shift = shift,
        seed = f"corner_one_{seed}"
    )
    
    rectangle = ruin_rectangle_random(
        length = segment_length, 
        width = width, 
        height = height,
        points = points[1],
        debug=debug,
        shift = shift,
        seed = f"rectangle_{seed}"
    )
    
    corner_two = ruin_corner_random(
        length = segment_length, 
        width = width, 
        height = height, 
        points = points[0],
        debug = debug,
        shift = shift,
        seed = f"corner_two_{seed}"
    )
    
    ruin_segment = (
        corner_one.translate((segment_length,0,0))
        .union(rectangle)
        .union(corner_two.rotate((0,1,0),(0,0,0),180).translate((0,0,height)))
    ).translate((-segment_length/2,0,0))
    
    return ruin_segment
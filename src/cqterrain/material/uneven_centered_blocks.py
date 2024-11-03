import cadquery as cq
from . import center_blocks 
from . import uneven_blocks


def uneven_centered_blocks(
    tile_length:float = 10, 
    tile_width:float = 5, 
    tile_height:float = 5, 
    rows:int = 5, 
    columns:int = 5, 
    margin:float  = 2,
    uneven_depth:float  = 2.5,
    seed:str = 'test',
    segments:int  = 5,
    peak_count:tuple[int,int]|int  = (4,5)
):

    blocks = uneven_blocks(
        tile_length = tile_length, 
        tile_width = tile_width, 
        tile_height= tile_height, 
        rows = rows, 
        columns = columns, 
        margin = margin,
        uneven_depth = uneven_depth,
        seed = seed,
        segments = segments,
        peak_count = peak_count
    )
    
    c_blocks = center_blocks(blocks)
    
    return c_blocks
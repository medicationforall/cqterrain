import cadquery as cq
from cqterrain.damage import uneven_plane

def uneven_blocks(
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
    ) -> cq.Workplane:
    
    block = cq.Workplane("XY").box(
        tile_length, 
        tile_width, 
        tile_height
    )
    
    t_length = tile_length +(margin * 2)
    t_width = tile_width +(margin * 2)

    length = t_length * columns
    width = t_width * rows
    
    def add_block(loc:cq.Location)->cq.Shape:
        return block.val().located(loc) #type:ignore
    
    blocks = result = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = t_length, 
            ySpacing = t_width,
            xCount = columns, 
            yCount= rows, 
            center = True)
        .eachpoint(callback = add_block)
    )
    
    uneven = uneven_plane(
        length = length, 
        width = width, 
        height = uneven_depth, 
        min_height = 0.0001,
        seed = seed,
        segments = segments,
        peak_count = peak_count
    )
    
    uneven = (
        uneven
        .translate((0,0,-tile_height/2+uneven_depth/2))
        .rotate((0,1,0),(0,0,0),180)
    )

    pattern_blocks = (
        blocks
        .cut(uneven)
    )
    
    return pattern_blocks
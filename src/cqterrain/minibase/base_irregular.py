import cadquery as cq
from . import circle, ellipse, hexagon, rectangle, slot
from cadqueryhelper import irregular_grid
import random

def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
    )

def base_irregular(
    base:cq.Workplane = circle(
        diameter = 40,
        height = 3, 
        taper = -1,
        render_magnet = True,  
        magnet_diameter = 3, 
        magnet_height = 2
    ),
    min_height:float = 1,
    max_height:float = 3.5,
    overlap:float = 20,
    col_size:float = 5,
    row_size:float = 8,
    max_columns:int = 2,
    max_rows:int = 2,
    passes_count:int = 3000,
    seed:str = "seed",
    tile_styles:list = [custom_item],
    debug:bool = False
):

    top = (
       base
       .faces("Z")
       .wires()
       .toPending()
       .extrude(max_height)
    )

    def rand_tile(length, width, height):
        tile_style = random.choice(tile_styles)
        tile = tile_style(length, width, height)
        return tile
    
    bounds = base.val().BoundingBox()
    xlen = bounds.xlen
    ylen = bounds.ylen
    zlen = bounds.zlen

    pattern = irregular_grid(
        length = xlen + overlap,
        width = ylen + overlap,
        height = min_height,
        col_size = col_size,
        row_size = row_size,
        
        max_columns = max_columns,
        max_rows = max_rows,
        
        max_height = max_height,
        align_z = True,
        include_outline = True,
        union_grid = True,
        passes_count = passes_count,
        seed = seed,
        make_item = rand_tile
    )
    
    z_translate = zlen/2
    ex_floor = pattern.translate((0,0,z_translate))
    
    if debug:
        return base.add(ex_floor).add(top)
    else:
        greeble_floor = ex_floor.intersect(top)
        return base.union(greeble_floor)
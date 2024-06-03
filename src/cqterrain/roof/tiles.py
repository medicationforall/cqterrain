import cadquery as cq
import math
from cadqueryhelper import grid

def tiles(
        tile:cq.Workplane, 
        face:cq.Workplane,
        x:float, 
        height:float, 
        t_length:float, 
        t_width:float, 
        angle:float, 
        odd_col_push:list = [0,0], 
        rows:int = 3, 
        debug:bool = False, 
        intersect:bool = True
    ):
    hyp = math.hypot(x, height)
    columns = math.floor(hyp / t_length)+4

    c_face = face
    plane = (
        c_face.wires()
        .toPending()
        .translate((3, 0, 0.0))
        .toPending()
        .loft()
    )

    tiles = (
        grid.make_grid(
            tile, 
            [t_length, t_width], 
            rows = rows, 
            columns = columns, 
            odd_col_push = odd_col_push
        )
        .rotate((0,1,0),(0,0,0),-angle)
        .translate(((x/4),0,0))
    )

    composite = (
        cq.Workplane("XY")
        .union(tiles)
    )

    if debug:
        combine = composite.union(plane)
    else:
        combine = composite.intersect(plane)

    if intersect:
        return combine
    else:
        return composite
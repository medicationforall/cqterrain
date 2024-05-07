import cadquery as cq
from .. import pipe as terrain_pipe

def pipe(
        length:float = 25, 
        width:float = 25, 
        height:float = 4,

        radius:float = 4,
        inner_radius:float = 3,
        segment_length:float = 6,
        space:float = 4
    ):

    outline = cq.Workplane("XY").box(length, width, height)

    tile_pipe = terrain_pipe.corrugated_straight(
        length, 
        radius, 
        inner_radius, 
        segment_length, 
        space
    )

    tile = (
        cq.Workplane("XY")
        .union(outline)
        .add(tile_pipe)
    )

    return tile




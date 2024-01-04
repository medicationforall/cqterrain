import cadquery as cq
from .. import pipe as terrain_pipe

def pipe(
        length = 25, 
        width = 25, 
        height = 4,

        radius = 4,
        inner_radius = 3,
        segment_length = 6,
        space = 4
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




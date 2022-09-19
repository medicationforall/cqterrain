import cadquery as cq
from cadqueryhelper import grid

def octagon_with_dots():
    tile = (cq.Workplane("XY")
            .rect(5,5)
            .extrude(1)
            .edges("|Z")
            .chamfer(1.2) # SET PERCENTAGE
            )

    rotated_tile = tile.rotate((0,0,1),(0,0,0), 45)

    mid_tile = (cq.Workplane("XY")
            .rect(1.6,1.6)
            .extrude(1)
            .rotate((0,0,1),(0,0,0), 45)
            )

    tiles = grid.make_grid(tile, [5.5,5.5], rows=3, columns=3)
    center_tiles = grid.make_grid(mid_tile, [5.5,5.5], rows=4, columns=4)

    combined = tiles.add(center_tiles).translate((0,0,-1*(1/2)))
    return combined


def basketweave(length = 4, width = 2, height = 1, padding = .5):
    length_padding = length + padding
    width_padding = width + padding
    rect = (
            cq.Workplane("XY")
            .box(width, length_padding, height)
            .center(width_padding, 0)
            .box(width, length_padding, height)
            .translate((-1*(width_padding/2), 0, 0))
            )

    rect2 = (
            cq.Workplane("XY")
            .box(width, length_padding, height)
            .center(width_padding, 0)
            .box(width, length_padding, height)
            .translate((-1*(width_padding/2), 0, 0))
            .rotate((0,0,1), (0,0,0), 90)
            .translate((width_padding*2, 0, 0))
        )

    combine = (cq.Workplane("XY").add(rect).add(rect2).translate((-1*(width_padding),0,0)))
    combine2 = (cq.Workplane("XY")
                .add(combine)
                .rotate((0,0,1),(0,0,0), 180)
                .translate((0,width_padding*2,0))
                )

    tile_combine = cq.Workplane("XY").add(combine).add(combine2).translate((0,-1*(width_padding),0))
    return tile_combine

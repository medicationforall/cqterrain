import cadquery as cq
from cadqueryhelper import grid

def octagon_with_dots(tile_size=5, chamfer_size = 1.2, mid_tile_size =1.6, spacing = .5 , tile_height = 1):
    tile = (cq.Workplane("XY")
            .rect(tile_size,tile_size)
            .extrude(tile_height)
            .edges("|Z")
            .chamfer(chamfer_size) # SET PERCENTAGE
            )


    mid_tile = (cq.Workplane("XY")
            .rect(mid_tile_size, mid_tile_size)
            .extrude(tile_height)
            .rotate((0,0,1),(0,0,0), 45)
            )

    tiles = (
        cq.Workplane("XY")
        .union(tile.translate((-1*((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(tile.translate((((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(tile.translate((((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
        .union(tile.translate((-1*((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
        .union(mid_tile)
        .union(mid_tile.translate((-1*((tile_size) + spacing),0,0)))
        .union(mid_tile.translate((((tile_size) + spacing),0,0)))
        .union(mid_tile.translate((0,-1*((tile_size) + spacing),0)))
        .union(mid_tile.translate((0,((tile_size) + spacing),0)))
        .union(mid_tile.translate((-1*((tile_size) + spacing),((tile_size) + spacing),0)))
        .union(mid_tile.translate((-1*((tile_size) + spacing),-1*((tile_size) + spacing),0)))
        .union(mid_tile.translate((((tile_size) + spacing),-1*((tile_size) + spacing),0)))
        .union(mid_tile.translate((((tile_size) + spacing),((tile_size) + spacing),0)))
    )
    return tiles.translate((0,0,-1*(tile_height/2)))


def octagon_with_dots_2(tile_size=5, chamfer_size = 1.2, mid_tile_size =1.6, spacing = .5 , tile_height = 1):
    tile = (cq.Workplane("XY")
            .box(tile_size,tile_size, tile_height)
            .edges("|Z")
            .chamfer(chamfer_size) # SET PERCENTAGE
            )


    mid_tile = (cq.Workplane("XY")
            .box(mid_tile_size, mid_tile_size, tile_height)
            .rotate((0,0,1),(0,0,0), 45)
            )

    tiles = (
        cq.Workplane("XY")
        .union(tile)
        .union(mid_tile.translate((-1*((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(mid_tile.translate((((tile_size/2) + spacing/2),((tile_size/2) + spacing/2),0)))
        .union(mid_tile.translate((((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
        .union(mid_tile.translate((-1*((tile_size/2) + spacing/2),-1*((tile_size/2) + spacing/2),0)))
    )

    cut_tile = cq.Workplane("XY").box(tile_size+spacing, tile_size+spacing, tile_height)
    return cut_tile.intersect(tiles).translate((0,0,-1*(tile_height/2)))


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

    combine = (cq.Workplane("XY").union(rect).union(rect2).translate((-1*(width_padding),0,0)))
    combine2 = (cq.Workplane("XY")
                .union(combine)
                .rotate((0,0,1),(0,0,0), 180)
                .translate((0,width_padding*2,0))
                )

    tile_combine = cq.Workplane("XY").union(combine).union(combine2).translate((0,-1*(width_padding),0))
    return tile_combine

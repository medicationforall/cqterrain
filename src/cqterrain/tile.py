import cadquery as cq
from cadqueryhelper import shape, grid

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
    return cut_tile.intersect(tiles)


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


def star(length=10, width=10, height=1, points=4, outer_radius=5, inner_radius=3, padding=.5):
    tile = cq.Workplane("XY").box(length, width, height)

    cut_star = shape.star(outer_radius=outer_radius+(padding/2), inner_radius=inner_radius+(padding/2), points=points, height=height)
    star = shape.star(outer_radius=outer_radius-(padding/2), inner_radius=inner_radius-(padding/2), points=points, height=height)

    return tile.cut(cut_star).add(star)


def windmill(tile_size=10, height=1, padding=.5):
    outline = cq.Workplane("XY").box(tile_size, tile_size, height)
    sq_size = (tile_size/3)-padding/2
    rec_size = ((tile_size/3)*2)
    square = cq.Workplane("XY").box(sq_size, sq_size, height)
    rectangle = cq.Workplane("XY").box(sq_size, rec_size, height)

    rec_tran = rectangle.translate((sq_size+padding,sq_size/2+padding/2,0))
    tile = (
        square
        .union(rec_tran)
        .union(rec_tran.rotate((0,0,1),(0,0,0),90))
        .union(rec_tran.rotate((0,0,1),(0,0,0),180))
        .union(rec_tran.rotate((0,0,1),(0,0,0),270))
    )
    return outline.intersect(tile)

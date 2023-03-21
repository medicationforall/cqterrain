import cadquery as cq
from cqterrain import tile

tile = tile.octagon_with_dots_2(
    tile_size = 5,
    chamfer_size = 1.2,
    mid_tile_size = 1.6,
    spacing = .5
)

cq.exporters.export(tile,'out/tile_octagon_with_dots.stl')

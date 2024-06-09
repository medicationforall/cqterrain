import cadquery as cq
from cqterrain import tile

result = tile.octagon_with_dots_2(
    tile_size = 5,
    chamfer_size = 1.2,
    mid_tile_size = 1.6,
    spacing = .5,
    tile_height = 1
)

cq.exporters.export(result,'stl/tile_octagon_with_dots.stl')

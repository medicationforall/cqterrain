import cadquery as cq
from cqterrain import tile

result = tile.star(
    length = 10,
    width = 10,
    height = 1,
    points = 4,
    outer_radius = 5,
    inner_radius = 3,
    padding = .5
)

cq.exporters.export(result,'out/tile_star.stl')

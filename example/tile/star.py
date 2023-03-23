import cadquery as cq
from cqterrain import tile

result = tile.star(
    length = 8.5,
    points = 9,
    inner_radius = 2,
    padding = 1
)

cq.exporters.export(result,'out/tile_star.stl')

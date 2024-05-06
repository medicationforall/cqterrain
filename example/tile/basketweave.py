import cadquery as cq
from cqterrain import tile

result = tile.basketweave(
    length = 4,
    width = 2,
    height = 1,
    padding = .5
)

cq.exporters.export(result,'stl/tile_basketweave.stl')

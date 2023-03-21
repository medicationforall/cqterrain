import cadquery as cq
from cqterrain import tile

tile = tile.basketweave(
    length = 4,
    width = 2,
    height = 1,
    padding = .5
)

cq.exporters.export(tile,'out/tile_basketweave.stl')

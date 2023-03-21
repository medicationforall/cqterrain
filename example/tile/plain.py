import cadquery as cq
from cqterrain import tile

tile = tile.plain(
    length = 10,
    width = 10,
    height = 2,
    padding = 1
)

cq.exporters.export(tile,'out/tile_plain.stl')

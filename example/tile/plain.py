import cadquery as cq
from cqterrain import tile

result = tile.plain(
    length = 10,
    width = 10,
    height = 2,
    padding = 1
)

cq.exporters.export(result,'out/tile_plain.stl')

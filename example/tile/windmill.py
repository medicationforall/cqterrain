import cadquery as cq
from cqterrain import tile

result = tile.windmill(
    tile_size = 10,
    height = 1,
    padding = 0.5
)

cq.exporters.export(result,'out/tile_windmill.stl')

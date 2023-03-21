import cadquery as cq
from cqterrain import tile

tile = tile.windmill(
    tile_size = 10,
    height = 1,
    padding = 0.5
)

cq.exporters.export(tile,'out/tile_windmill.stl')

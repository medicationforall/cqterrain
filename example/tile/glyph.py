import cadquery as cq
from cqterrain import tile

result = tile.glyph(
    length = 4,
    width = 2,
    height = 1,
    padding = .5
)

cq.exporters.export(result,'stl/tile_glyph.stl')

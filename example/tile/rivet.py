import cadquery as cq
from cqterrain import tile

result = tile.rivet(
    length = 10,
    width = 10,
    height = 2,
    padding = 1,
    internal_padding = 2.5,
    rivet_height = 2.5,
    rivet_radius = .5
)

cq.exporters.export(result,'stl/tile_rivet.stl')

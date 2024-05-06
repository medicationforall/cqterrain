import cadquery as cq
from cqterrain import tile

result = tile.rivet_round(
    radius = 10, 
    height = 2,
    rivet_height = 0.5,
    rivet_radius = .5,
    padding = 1,
    rivet_count = 5
)

cq.exporters.export(result,'stl/tile_rivet_round.stl')
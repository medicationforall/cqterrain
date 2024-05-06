import cadquery as cq
from cqterrain import tile

result = tile.charge(
    length = 30, 
    width = 25, 
    height = 4,
    line_width = 3,
    line_depth = 1,
    corner_chamfer = 4,
    edge_chamfer = 2,
    padding = 2.5
)

#show_object(result)
cq.exporters.export(result,'stl/tile_charge.stl')
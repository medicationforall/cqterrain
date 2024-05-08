import cadquery as cq
from cqterrain.tile import truchet_circle

result = truchet_circle(
    length = 10,
    width = 10,
    height = 4,
    radius = 1.5, 
    base_height = 2,
    shift_design=0
)
#show_object(result)
cq.exporters.export(result,'stl/tile_truchet_circle.stl')

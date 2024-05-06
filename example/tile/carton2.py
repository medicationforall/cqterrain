import cadquery as cq
from cqterrain import tile

result = tile.carton2(
    length = 30, 
    width = 25, 
    height = 4, 
    line_width = 2, 
    line_depth = 1.5,
    x_divisor = 2,
    y_divisor = 3
)
#show_object(result)

cq.exporters.export(result,'stl/tile_carton2.stl')
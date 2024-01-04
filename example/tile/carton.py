import cadquery as cq
from cqterrain import tile

result = tile.carton(
    length=60, 
    width=60, 
    height = 4,
    line_width = 3,
    line_depth = 1.5,
    x_divisor = 3,
    y_divisor = 2
)
#show_object(result)

cq.exporters.export(result,'out/tile_carton.stl')
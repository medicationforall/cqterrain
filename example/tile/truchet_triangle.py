import cadquery as cq
from cqterrain import tile

result = tile.truchet_triangle(
    length = 10, 
    width = 10, 
    height = 4, 
    min_height = 2
)

#show_object(result)
cq.exporters.export(result,'stl/tile_truchet_triangle.stl')

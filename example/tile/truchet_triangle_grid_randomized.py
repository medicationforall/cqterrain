import cadquery as cq
from cadqueryhelper.grid import randomized_rotation_grid
from cqterrain import tile

triangle_tile = tile.truchet_triangle(
    length = 10, 
    width = 10, 
    height = 4, 
    min_height = 2
)

result = randomized_rotation_grid(
        shape = triangle_tile, 
        seed = "test3",
        rotate_increment = 90, 
        rotate_min = 0, 
        rotate_max = 360,
        x_count = 5,
        y_count = 5,
        x_spacing = 10,
        y_spacing = 10
)

#show_object(result)
cq.exporters.export(result,'stl/tile_truchet_triangle_randomized_grid.stl')



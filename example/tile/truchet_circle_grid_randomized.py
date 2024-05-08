import cadquery as cq
from cqterrain.tile import truchet_circle
from cadqueryhelper import randomized_rotation_grid

example_tile = truchet_circle(
    length=20,
    width=20,
    height=4,
    radius=2, 
    base_height=2.5,
    shift_design=3
)
#show_object(example_tile)

#---------------------
random_grid = randomized_rotation_grid(
    example_tile,
    x_spacing=20,
    y_spacing=20,
    x_count=10,
    y_count=10,
    seed='truchet'
)
result = cq.Workplane('XY').union(random_grid)
#show_object(union_grid)

cq.exporters.export(result,'stl/tile_truchet_circle_randomized_grid.stl')

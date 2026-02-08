import cadquery as cq
import random
from cqterrain import tile
from cadqueryhelper.grid import randomized_rotation_grid, scheme_grid, rotate_grid

#-----------------------
# Tile
triangle_tile = tile.truchet_triangle()
tile_text = cq.Workplane("XY").text('Tile',10,3)

#-----------------------
# Grid
def add_star(loc:cq.Location) -> cq.Shape:
    return triangle_tile.val().located(loc) #type: ignore

result = (
    cq.Workplane("XY")
    .rarray(
        xSpacing = 10, 
        ySpacing = 10,
        xCount = 5, 
        yCount= 5, 
        center = True)
    .eachpoint(add_star)
)

union_grid = cq.Workplane("XY").union(result)
grid_text = cq.Workplane("XY").text('Grid',10,3)

#-----------------------
# Rotate grid   
rotate_example = rotate_grid(triangle_tile)
union_rotate = cq.Workplane("XY").union(rotate_example)
rotate_grid_text = cq.Workplane("XY").text('Rotate Grid',10,3)

#-----------------------
# Randomized Rotation Grid
rotate_example = randomized_rotation_grid(triangle_tile, 'test3')
union_randomized = cq.Workplane("XY").union(rotate_example)
randomized_text = cq.Workplane("XY").text('Randomized',10,3)

#-----------------------
# Schema Grid
scheme_example = scheme_grid(triangle_tile)
union_scheme = cq.Workplane("XY").union(scheme_example)
scheme_text = cq.Workplane("XY").text('Scheme',10,3)

#-----------------------
# Schema Grid
scheme_example_2 = scheme_grid(
    shape=triangle_tile, 
    rotates=[-90,0,-180,-270,90,180,0],
    x_count=4,
    y_count=4,
    x_spacing = 10,
    y_spacing = 10,
    x_repeat=2,
    y_repeat=2,
)

union_scheme_2 = cq.Workplane("XY").union(scheme_example_2)
scheme_text_2 = cq.Workplane("XY").text('Scheme_2',10,3)

#----------------------

scene = (
    cq.Workplane()
    .union(triangle_tile.translate((-40,0,0)))
    .union(tile_text.translate((-40,-15,0)))

    .union(union_grid)
    .union(grid_text.translate((0,-35,0)))

    .union(union_rotate.translate((0,50,0)))
    .union(rotate_grid_text.translate((0,80,0)))

    .union(union_randomized.translate((70,0,0)))
    .union(randomized_text.translate((70,-35,0)))

    .union(union_scheme.translate((130,0,0)))
    .union(scheme_text.translate((130,-35,0)))

    .union(union_scheme_2.translate((200,0,0)))
    .union(scheme_text_2.translate((200,-50,0)))
)

#show_object(scene)
cq.exporters.export(scene,'stl/tile_truchet_triangle_grids.stl')
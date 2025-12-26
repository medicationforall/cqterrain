import cadquery as cq
from cqterrain.ruin import three_wall_corner

ex_three_wall_corner = three_wall_corner(
    length = 60, 
    width = 80, 
    height = 75, 
    wall_width = 10
)

#show_object(result)
cq.exporters.export(ex_three_wall_corner, 'stl/ruin_three_wall_corner.stl')
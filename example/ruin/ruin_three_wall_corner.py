import cadquery as cq
from cqterrain.ruin import ruin_three_wall_corner

ex_three_wall_corner = ruin_three_wall_corner(
    length = 60, 
    width = 80, 
    height = 75, 
    wall_width = 10,
    base_points = 5,
    base_adjustments = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
    x_points = 6,
    x_adjustments = [(10,-5),(-2,-2),(3,5)],
    y_points = 4,
    y_adjustments = [(10,-5),(-2,-2),(3,5),(-3,5)]
)

#show_object(result)
cq.exporters.export(ex_three_wall_corner, 'stl/ruin_ruin_three_wall_corner.stl')
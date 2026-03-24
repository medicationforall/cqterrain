import cadquery as cq
from cqterrain.ruin import ruin_three_wall_section

ex_ruin = ruin_three_wall_section(
    length = 50, 
    width = 50, 
    height = 50, 
    wall_width = 5,
    base_points = 5,
    base_adjustments = [(10,-5),(-2,-2),(3,5),(-10,-10),(0,3)],
    x_points = 3,
    x_adjustments = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
    x_points_two = 4,
    x_adjustments_two = [(10,-5),(-2,-2),(3,5),(-5,-3),(0,3)],
    y_points = 4,
    y_adjustments = [(10,-20),(-2,-2),(3,5),(-10,-7),(0,3)],
    debug = False
)

#show_object(ex_ruin)

cq.exporters.export(ex_ruin, 'stl/ruin_three_wall_section.stl')
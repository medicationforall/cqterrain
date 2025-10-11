import cadquery as cq
from cqterrain.minibase import ellipse_wood

ex_base = ellipse_wood(    
    x_diameter = 52, 
    y_diameter = 90, 
    base_height = 3,
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    board_height = 1,
    overlap = 20,
    seed = "seed",
    joist_space = 12.5,
    board_width = 6.5,
    board_width_spacer = .2,
    board_break_width = .4,
    nail_diameter = .6,
    joist_width = 4,
    debug = False
)

#show_object(ex_base)
cq.exporters.export(ex_base,'stl/minibase_ellipse_wood.stl')
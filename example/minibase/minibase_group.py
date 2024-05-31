import cadquery as cq
from cqterrain.minibase import (
    ellipse, 
    circle, 
    rectangle, 
    slot,
    hexagon
)

#------------------
ellipse_base = ellipse(
    x_diameter=52, 
    y_diameter=90, 
    height=3, 
    taper=-1,
    render_magnet = True, 
    magnet_diameter=3, 
    magnet_height=2
)

#show_object(ellipse_base)

#--------------------
circle_base = circle(
    diameter=25, 
    height=3, 
    taper=-1,
    render_magnet = True, 
    magnet_diameter=3, 
    magnet_height=2
)

#show_object(circle_base)

#--------------------
rectangle_base = rectangle(
    length = 25, 
    width = 25, 
    height = 3, 
    taper = -1,
    render_magnet = True, 
    magnet_diameter = 3, 
    magnet_height = 2
)

#show_object(rectangle_base)

#---------------------

slot_base = slot(
    length = 24, 
    width = 50, 
    height = 3, 
    taper = -1, 
    render_magnet = True, 
    magnet_diameter = 3, 
    magnet_height = 2
)

#show_object(slot_base)


#-----------------------

hexagon_base = hexagon(
    diameter = 25,
    height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2
)

#show_object(hexagon_base)


#-----------------------

group = (
    cq.Workplane("XY")
    .add(ellipse_base.translate((45,0,0)))
    .add(circle_base.translate((0,-30,0)))
    .add(rectangle_base.translate((0,30,0)))
    .add(slot_base.translate((-30,0,0)))
    .add(hexagon_base)
)

#show_object(group)
cq.exporters.export(group,'stl/minibase_group.stl')
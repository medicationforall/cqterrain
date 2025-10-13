import cadquery as cq
from cqterrain.minibase import (
    ellipse_wood, 
    circle_wood, 
    rectangle_wood, 
    slot_wood,
    hexagon_wood
)

seed = 'random_badger'

#------------------
ellipse_base = ellipse_wood(
    x_diameter=52, 
    y_diameter=90, 
    base_height=3, 
    taper=-1,
    render_magnet = True, 
    magnet_diameter=3, 
    magnet_height=2,
    seed = seed+"_one"
)

#show_object(ellipse_base)

#--------------------
circle_base = circle_wood(
    diameter=25, 
    base_height=3, 
    taper=-1,
    render_magnet = True, 
    magnet_diameter=3, 
    magnet_height=2,
    seed = seed+"_two"
)

#show_object(circle_base)

#--------------------
rectangle_base = rectangle_wood(
    length = 25, 
    width = 25, 
    base_height = 3, 
    taper = -1,
    render_magnet = True, 
    magnet_diameter = 3, 
    magnet_height = 2,
    seed = seed+"_three"
)

#show_object(rectangle_base)

#---------------------

slot_base = slot_wood(
    length = 50, 
    width = 24, 
    base_height = 3, 
    taper = -1, 
    render_magnet = True, 
    magnet_diameter = 3, 
    magnet_height = 2,
    seed = seed+"_four"
)

#show_object(slot_base)


#-----------------------

hexagon_base = hexagon_wood(
    diameter = 25,
    base_height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    seed = seed+"_five"
)

#show_object(hexagon_base)


#-----------------------

group = (
    cq.Workplane("XY")
    .add(ellipse_base.translate((45,0,0)))
    .add(circle_base.translate((0,-30,0)))
    .add(rectangle_base.translate((0,30,0)))
    .add(slot_base.translate((-40,0,0)))
    .add(hexagon_base)
)

#show_object(group)
cq.exporters.export(group,'stl/minibase_group_wood.stl')
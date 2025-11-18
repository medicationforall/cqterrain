import cadquery as cq
from cqterrain.minibase import (
    RuinStoneBase
)

seed = 'road_to'

#------------------
bp_ellipse_base = RuinStoneBase()
bp_ellipse_base.base_type = "ellipse"
bp_ellipse_base.diameter = 52 
bp_ellipse_base.diameter_y = 90 
bp_ellipse_base.height = 3
bp_ellipse_base.taper = -1
bp_ellipse_base.render_magnet = True 
bp_ellipse_base.magnet_diameter = 3 
bp_ellipse_base.magnet_height = 2
bp_ellipse_base.seed = seed+"_one"
bp_ellipse_base.make()
ellipse_base = bp_ellipse_base.build()

#show_object(ellipse_base)

#--------------------
bp_circle_base = RuinStoneBase()
bp_circle_base.base_type = "circle"
bp_circle_base.diameter = 25 
bp_circle_base.height=3
bp_circle_base.taper=-1
bp_circle_base.render_magnet = True 
bp_circle_base.magnet_diameter=3
bp_circle_base.magnet_height=2
bp_circle_base.seed = seed+"_two"
bp_circle_base.make()
circle_base = bp_circle_base.build()

#show_object(circle_base)

#--------------------
bp_rectangle_base = RuinStoneBase()
bp_rectangle_base.base_type = "rectangle"
bp_rectangle_base.length = 25
bp_rectangle_base.width = 25
bp_rectangle_base.height = 3
bp_rectangle_base.taper = -1
bp_rectangle_base.render_magnet = True 
bp_rectangle_base.magnet_diameter = 3
bp_rectangle_base.magnet_height = 2
bp_rectangle_base.seed = seed+"_three"
bp_rectangle_base.make()
rectangle_base = bp_rectangle_base.build()


#show_object(rectangle_base)

#---------------------

bp_slot_base = RuinStoneBase()
bp_slot_base.base_type = "slot"
bp_slot_base.length = 50
bp_slot_base.width = 24 
bp_slot_base.height = 3 
bp_slot_base.taper = -1
bp_slot_base.render_magnet = True
bp_slot_base.magnet_diameter = 3
bp_slot_base.magnet_height = 2
bp_slot_base.seed = seed+"_four"
bp_slot_base.make()
slot_base = bp_slot_base.build()

#show_object(slot_base)

#-----------------------

bp_hexagon_base = RuinStoneBase()
bp_hexagon_base.base_type = "hexagon"
bp_hexagon_base.diameter = 25
bp_hexagon_base.height = 3 
bp_hexagon_base.taper = -1
bp_hexagon_base.render_magnet = True
bp_hexagon_base.magnet_diameter = 3
bp_hexagon_base.magnet_height = 2
bp_hexagon_base.seed = seed+"_five"
bp_hexagon_base.make()
hexagon_base = bp_hexagon_base.build()


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
cq.exporters.export(group,'stl/minibase_group_ruin.stl')
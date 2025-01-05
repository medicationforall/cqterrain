import cadquery as cq
from cqterrain.shieldwall import  ShieldShape

shape_bp = ShieldShape()

shape_bp.length = 20
shape_bp.width = 20
shape_bp.base_height = 5.6
shape_bp.middle_width_inset = -6
shape_bp.travel_distance = 2

shape_bp.make()

shape_ex = shape_bp.build().extrude(2)
#show_object(shape_ex)

cq.exporters.export(shape_ex, 'stl/shieldwall_shield_shape.stl')
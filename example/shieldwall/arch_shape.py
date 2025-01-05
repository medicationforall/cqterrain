import cadquery as cq
from cqterrain.shieldwall import ArchShape

bp_shape = ArchShape()
bp_shape.length = 25
bp_shape.width = 20
bp_shape.base_height = 5
bp_shape.middle_width_inset = -6

bp_shape.make()

result = bp_shape.build().extrude(1)

#show_object(result)
cq.exporters.export(result, 'stl/shieldwall_arch_shape.stl')
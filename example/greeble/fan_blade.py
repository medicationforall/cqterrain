import cadquery as cq
from cqterrain.greeble import FanBlade

bp_fan = FanBlade()

bp_fan.diameter = 15
bp_fan.height = 5
bp_fan.cylinder_height = 2.5
bp_fan.cylinder_diameter = 5
bp_fan.blade_width = 1
bp_fan.blade_rotate = 23
bp_fan.blade_count = 3
bp_fan.debug = False
bp_fan.shift_rotate = 10
bp_fan.shift_translate = .5

bp_fan.make()

ex_fan = bp_fan.build()
#show_object(ex_fan)

cq.exporters.export(ex_fan, 'stl/greeble_fan_blade.stl')
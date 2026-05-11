import cadquery as cq
from cqterrain.greeble import FanIndustrial

bp_fan = FanIndustrial()
bp_fan.length = 30
bp_fan.width = 25
bp_fan.height = 20
bp_fan.diameter = 40
bp_fan.housing_inner_diameter = 4
bp_fan.fan_cylinder_diameter = 10
bp_fan.fin_width = 1.5
bp_fan.fin_length = 1.5
bp_fan.fin_count = 6
bp_fan.housing_wall_cut_width = 2
bp_fan.housing_wall_height = 3
bp_fan.blade_count = 14
bp_fan.shift_rotate = 10
bp_fan.blade_width = 3
bp_fan.blade_rotate = 25

bp_fan.make()

ex_fan = bp_fan.build()
#show_object(ex_fan)

cq.exporters.export(ex_fan, 'stl/greeble_fan_industrial.stl')
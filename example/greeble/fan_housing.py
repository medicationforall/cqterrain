import cadquery as cq
from cqterrain.greeble import FanHousing

bp_fan = FanHousing()

bp_fan.diameter = 10
bp_fan.height = 5

#housing
bp_fan.housing_inner_diameter = 2
bp_fan.housing_wall_cut_width = 1
bp_fan.housing_wall_height = 1
bp_fan.housing_wall_chamfer = 0.499

#fin
bp_fan.render_fins = True
bp_fan.fin_length = 0.5
bp_fan.fin_width = 0.5
bp_fan.fin_count = 3

bp_fan.make()

ex_fan = bp_fan.build()
#show_object(ex_fan)

cq.exporters.export(ex_fan, 'stl/greeble_fan_housing.stl')
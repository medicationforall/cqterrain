import cadquery as cq
from cqterrain.greeble import Dish

bp_dish = Dish()

bp_dish.length = 40
bp_dish.width = 23
bp_dish.height = 2
bp_dish.short_length = None
bp_dish.rotate = 0
bp_dish.diameter = 28
bp_dish.outer_diameter = 70

bp_dish.render_connector = True
bp_dish.connector_diameter = 5
bp_dish.connector_length = 2
bp_dish.connector_cylinder_diameter = 3
bp_dish.connector_cylinder_length = 4
bp_dish.connector_height = 4

bp_dish.dish_render = True
bp_dish.dish_z_translate = 0.2

bp_dish.render_mount = True
bp_dish.mount_length = 6

bp_dish.render_collector = True
bp_dish.collector_horn_height = 5
bp_dish.collector_horn_diameter = 4
bp_dish.collector_arm_length = 2
bp_dish.collector_arm_width = 2
bp_dish.collector_arm_height = 14
bp_dish.collector_arm_rotate = -37
bp_dish.collector_z_translate = 15.9

bp_dish.make()
ex_dish = bp_dish.build()

#show_object(ex_dish)
cq.exporters.export(ex_dish, 'stl/greeble_dish.stl')
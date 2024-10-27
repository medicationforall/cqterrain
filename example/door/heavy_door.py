import cadquery as cq
from cqterrain.door import HeavyDoor

bp_door = HeavyDoor()
bp_door.length = 30 
bp_door.width =  4
bp_door.height = 45
bp_door.trim_size = 1.5
bp_door.inset_depth = 1

bp_door.render_side_cuts = True

bp_door.side_cut_height = 20 
bp_door.side_cut_length = 5
bp_door.side_cut_distance = 5
bp_door.side_cut_operation = 'chamfer'

bp_door.render_cross_bars = True
bp_door.cross_bars_angle = 30
bp_door.cross_bar_offset = 8
bp_door.cross_bar_height = None

bp_door.render_window = True
bp_door.make()

ex_door = bp_door.build_plate()

#show_object(ex_door
cq.exporters.export(ex_door,'stl/door_heavy_door.stl')
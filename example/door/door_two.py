import cadquery as cq
from  cqterrain.door import DoorTwo

bp_door = DoorTwo()

bp_door.length = 30
bp_door.width = 2
bp_door.height = 40

bp_door.greeble_length = 5
bp_door.greeble_width = 3
bp_door.greeble_height = 12
bp_door.greeble_inner_height = 4
bp_door.greeble_z_translate = -3

bp_door.chamfer = (3.5,3.5)
bp_door.side_chamfer = .5

bp_door.render_window = True
bp_door.window_length = 6
bp_door.window_width = 3
bp_door.window_height = 3
bp_door.window_frame_width = 1
bp_door.window_z_translate = 30

bp_door.hinge_offset = 3
bp_door.hinge_chamfer = 1

bp_door.make()
result = bp_door.build()

#show_object(result)
cq.exporters.export(result,'stl/door_two.stl')
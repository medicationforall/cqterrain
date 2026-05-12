import cadquery as cq
from  cqterrain.door import DoorDouble

bp_door = DoorDouble()
bp_door.length = 60
bp_door.width = 3
bp_door.height = 40

bp_door.frame_width = 3
bp_door.chamfer = 5
bp_door.cut_chamfer = 3.5

bp_door.window_length = 6
bp_door.window_height = 3
bp_door.window_z_translate = 30

bp_door.make()
result = bp_door.build()

#show_object(result)
cq.exporters.export(result,'stl/door_double.stl')
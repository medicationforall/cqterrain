import cadquery as cq
from  cqterrain  import Door

bp_door = Door()
bp_door.length = 25
bp_door.width = 8
bp_door.frame_length = 3 
bp_door.frame_height = 4
bp_door.inner_width = 3
bp_door.height  = 40
bp_door.x_offset = 0

bp_door.make()
result = bp_door.build()

#show_object(result)
cq.exporters.export(result,'stl/door.stl')

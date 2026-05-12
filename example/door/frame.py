import cadquery as cq
from  cqterrain.door import Frame

bp_frame = Frame()
bp_frame.length = 60
bp_frame.width = 3
bp_frame.height = 40

bp_frame.frame_width = 3
bp_frame.chamfer = 5
bp_frame.cut_chamfer = 3.5

bp_frame.make()
result = bp_frame.build()

#show_object(result)
cq.exporters.export(result,'stl/door_frame.stl')
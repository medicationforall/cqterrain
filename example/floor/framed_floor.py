import cadquery as cq
from cqterrain.floor import FramedFloor

bp_floor = FramedFloor()

bp_floor.length = 75
bp_floor.width = 75
bp_floor.height = 4
bp_floor.frame_width = 2
bp_floor.corner_chamfer = 8
bp_floor.corner_fillet = None

bp_floor.make()

ex_floor = bp_floor.build()

#show_object(ex_floor)

cq.exporters.export(ex_floor, 'stl/floor_framed_floor.stl')
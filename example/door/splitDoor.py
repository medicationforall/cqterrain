import cadquery as cq
from cqterrain.door import SplitDoor

bp = SplitDoor()
bp.width = 24
bp.width = 2
bp.chamfer_minus = 0.1
bp.height = 56
bp.base_height = 32.5
bp.open=5
bp.bar_height = 1

bp.make()

door_ex = bp.build()

#show_object(door_ex)
cq.exporters.export(door_ex,'stl/door_splitDoor.stl')

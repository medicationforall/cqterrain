import cadquery as cq
from cqterrain.door import GarageDoor

bp_door = GarageDoor()

bp_door.render_frame:bool = True
bp_door.render_door:bool = True
bp_door.render_clamps:bool = True
bp_door.render_panel:bool = True

bp_door.make()

ex_door = bp_door.build()

#show_object(ex_door)
cq.exporters.export(ex_door, "stl/door_garage_door.stl")
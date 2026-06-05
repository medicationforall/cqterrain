import cadquery as cq
from cqterrain.door import PanelDoor

bp_door = PanelDoor()

bp_door.length = 100
bp_door.width = 5
bp_door.height = 52

bp_door.panel_count = 3

bp_door.render_windows = True
bp_door.window_count = 2
bp_door.window_length = 12
bp_door.window_height = 6
bp_door.window_frame = 1.5
bp_door.window_frame_width = 1

bp_door.render_rollers = True
bp_door.roller_length = 3
bp_door.roller_height = 4

bp_door.make()

ex_door = bp_door.build()

#show_object(ex_door)
cq.exporters.export(ex_door,'stl/door_panel_door.stl')
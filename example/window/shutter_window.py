import cadquery as cq
from  cqterrain.window import ShutterWindow

bp_window = ShutterWindow()

bp_window.length = 50
bp_window.width = 4
bp_window.height = 25

bp_window.frame_width = 4
bp_window.pane_count = 2
bp_window.louver_count = 5
bp_window.louver_rotate = 16

bp_window.make()
result = bp_window.build()

#show_object(result)
cq.exporters.export(result,'stl/window_shutter_window.stl')
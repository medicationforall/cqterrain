import cadquery as cq
from  cqterrain.window import Shutter

bp_window = Shutter()
bp_window.length = 25
bp_window.width = 2
bp_window.height = 30
bp_window.louver_count  = 5
bp_window.louver_rotate  = 16

bp_window.make()
result = bp_window.build()

#show_object(result)
cq.exporters.export(result,'stl/window_shutter.stl')
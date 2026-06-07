import cadquery as cq
from cqterrain.greeble import Panel

bp_panel = Panel()

bp_panel.length = 8
bp_panel.width = 6
bp_panel.height = 35
bp_panel.outer_height = 15

bp_panel.frame = 1.5
bp_panel.frame_depth = 1

bp_panel.make()

ex_panel = bp_panel.build()

#show_object(ex_panel)
cq.exporters.export(ex_panel, 'stl/greeble_panel.stl')
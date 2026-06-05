import cadquery as cq
from cqterrain.greeble import BottomClamps

bp_clamps = BottomClamps()

bp_clamps.length = 100
bp_clamps.width = 8
bp_clamps.height = 2

bp_clamps.clamp_height = 7
bp_clamps.clamp_chamfer = 1
bp_clamps.clamp_count = 3
bp_clamps.clamp_width = 8
bp_clamps.clamp_bottom_length = 25
bp_clamps.clamp_top_length = 10

bp_clamps.make()

ex_clamps = bp_clamps.build()

#show_object(ex_clamps)
cq.exporters.export(ex_clamps, 'stl/greeble_bottom_clamps.stl')
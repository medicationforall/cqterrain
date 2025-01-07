import cadquery as cq
from cqterrain.door import Hatch

bp = Hatch()

bp.length = 25
bp.width = 25
bp.height = 4
bp.base_corner_chamfer = 2
bp.base_top_chamfer = 2
bp.base_extrude = 1.5

bp.hatch_radius = 10.5
bp.hatch_height = 1.5
bp.hatch_chamfer = 0.8
bp.cross_bar_width = 4
bp.inner_ring_width = 2.5
bp.cut_out_chamfer = 0.3

bp.make()
hatch_ex = bp.build()
#show_object(hatch_ex)
cq.exporters.export(hatch_ex,'stl/door_hatch.stl')

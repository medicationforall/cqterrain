import cadquery as cq
from cqterrain.swivel import SwivelBase

bp = SwivelBase()

bp.diameter = 30
bp.height = 6
bp.chamfer = 1.5
bp.top_width = 2
bp.channel_width = 1

bp.magnet_diameter = 3.2
bp.magnet_height = 2.4
bp.cut_height = None

bp.render_greeble = True
bp.greeble_count = 6

bp.make()
ex_base = bp.build()

#show_object(ex_base)
cq.exporters.export(ex_base,"stl/swivel_base.stl")
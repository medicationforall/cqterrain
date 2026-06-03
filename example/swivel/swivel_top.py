import cadquery as cq
from cqterrain.swivel import SwivelTop

bp = SwivelTop()

bp.diameter = 30
bp.height = 3

bp.magnet_diameter = 3.2
bp.magnet_height = 2.4

bp.make()
ex_top = bp.build()

#show_object(ex_top)
cq.exporters.export(ex_top,"stl/swivel_top.stl")
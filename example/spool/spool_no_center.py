import cadquery as cq
from cqterrain.spool import Spool

bp = Spool()
bp.height = 100
bp.radius = 100
bp.wall_width = 3
bp.cut_radius = 40
bp.internal_wall_width = 4
#bp.internal_z_translate = -3
bp.make()
ex = bp.build_no_center()

#show_object(ex)

cq.exporters.export(ex,"stl/spool_no_center.stl")
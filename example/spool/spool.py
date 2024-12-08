import cadquery as cq
from cqterrain.spool import Spool

bp = Spool()
bp.height = 60
bp.radius = 80
bp.wall_width = 3
bp.cut_radius = 30
bp.internal_wall_width = 3
bp.internal_z_translate = 0
bp.make()
ex = bp.build()

#show_object(ex)

cq.exporters.export(ex,"stl/spool.stl")
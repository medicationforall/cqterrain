import cadquery as cq
from cqterrain.minibase import PointGridBase

bp_base = PointGridBase()
bp_base.length = 50
bp_base.width = 50
bp_base.diameter = 50
bp_base.base_type = "hexagon"
bp_base.debug = False
bp_base.make()
ex_base = bp_base.build()

#show_object(ex_base)

cq.exporters.export(ex_base, 'stl/minibase_point_grid_base.stl')
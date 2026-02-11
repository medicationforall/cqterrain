import cadquery as cq
from cqterrain.minibase import BasaltBase

bp_base = BasaltBase()
bp_base.length = 25
bp_base.width = 25
bp_base.diameter = 25
bp_base.detail_height = 10
bp_base.base_type = "rectangle"
bp_base.debug = False
bp_base.seed = "flower5"
bp_base.make()
ex_base = bp_base.build()

ex_pattern = bp_base.bp_grid.build()

#show_object(ex_base)
cq.exporters.export(ex_base,'stl/minibase_basalt_base.stl')
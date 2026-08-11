import cadquery as cq
from cqterrain.minibase import IndustrialGreebleBase

# circular Base
bp_base = IndustrialGreebleBase()
bp_base.base_type = "circle"
bp_base.diameter = 50
bp_base.seed = "test"
bp_base.render_uneven = False
bp_base.detail_height = 2
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.col_size = 10
bp_base.row_size = 10

bp_base.make()

ex_base = bp_base.build()
#show_object(ex_base)

cq.exporters.export(ex_base,"stl/minibase_circle_industrial.stl")
import cadquery as cq
from cqterrain.minibase import IndustrialGreebleBase

# Rectangle Base
bp_base = IndustrialGreebleBase()
bp_base.base_type = "rectangle"
bp_base.length = 40
bp_base.width = 40
bp_base.seed = f"rectangle_test"
bp_base.render_uneven = False
bp_base.detail_height = 2
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.col_size = 10
bp_base.row_size = 10

bp_base.make()
ex_base = bp_base.build()
#show_object(ex_base)

cq.exporters.export(ex_base,"stl/minibase_rectangle_industrial.stl")
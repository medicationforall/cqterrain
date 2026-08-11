import cadquery as cq
from cqterrain.minibase import IndustrialGreebleBase

seed = 'eva'

# Elipse base
#x_diameter=52, 
#y_diameter=90,

bp_base = IndustrialGreebleBase()
bp_base.base_type = "ellipse"
bp_base.diameter = 52 
bp_base.diameter_y = 90 
bp_base.seed = f"{seed}_ellipse_test"
bp_base.render_uneven = False
bp_base.detail_height = 2
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.col_size = 10
bp_base.row_size = 10

bp_base.make()
ellipse_base = bp_base.build()

#-----------------
# Circular Base
# diameter=25 

bp_base = IndustrialGreebleBase()
bp_base.base_type = "circle"
bp_base.diameter = 25
bp_base.seed = f"{seed}_round"
bp_base.render_uneven = False
bp_base.detail_height = 2
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.col_size = 10
bp_base.row_size = 10

bp_base.make()
circle_base = bp_base.build()

#----------------

# Rectangle Base
# length = 25 
# width = 25

bp_base = IndustrialGreebleBase()
bp_base.base_type = "rectangle"
bp_base.length = 25
bp_base.width = 25
bp_base.seed = f"{seed}_rectangle"
bp_base.render_uneven = False
bp_base.detail_height = 2
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.col_size = 10
bp_base.row_size = 10

bp_base.make()
rectangle_base = bp_base.build()

#------------------
# slot Base
# length = 24 
# width = 50 

bp_base = IndustrialGreebleBase()
bp_base.base_type = "slot"
bp_base.length = 50
bp_base.width = 24 
bp_base.seed = f"{seed}_slot"
bp_base.render_uneven = False
bp_base.detail_height = 2
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.col_size = 10
bp_base.row_size = 10

bp_base.make()
slot_base = bp_base.build()

#-----------------
# Hexagon Base
# diameter = 25,

bp_base = IndustrialGreebleBase()
bp_base.base_type = "hexagon"
bp_base.diameter = 25
bp_base.seed = f"{seed}_hexagon"
bp_base.render_uneven = False
bp_base.detail_height = 2
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.col_size = 10
bp_base.row_size = 10

bp_base.make()
hexagon_base = bp_base.build()

#-----------------

group = (
    cq.Workplane("XY")
    .add(ellipse_base.translate((45,0,0)))
    .add(circle_base.translate((0,-30,0)))
    .add(rectangle_base.translate((0,30,0)))
    .add(slot_base.translate((-40,0,0)))
    .add(hexagon_base)
)

#show_object(group)
cq.exporters.export(group,'stl/minibase_group_industrial_greeble.stl')

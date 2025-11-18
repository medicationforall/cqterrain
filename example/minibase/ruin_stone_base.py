import cadquery as cq
from cqterrain.minibase import RuinStoneBase

def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
    )

def custom_item_rotated_y_pos(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
        .rotate((0,1,0),(0,0,0),12)
    )

def custom_item_rotated_y_neg(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-.3, width-.3, height)
        .chamfer(0.5)
        .rotate((0,1,0),(0,0,0),-12)
    )

bp_base = RuinStoneBase()
bp_base.length = 30
bp_base.width = 25
bp_base.height = 3
bp_base.diameter = 30
bp_base.diameter_y = 30
bp_base.taper = -1
bp_base.magnet_diameter = 3
bp_base.magnet_height = 2
bp_base.render_magnet = True

bp_base.base_type= "circle"

bp_base.uneven_height = 4
bp_base.peak_count = (9,10)
bp_base.segments = 6
bp_base.seed = "seed"
bp_base.detail_height = 3

bp_base.overlap = 20
bp_base.min_height = 1
bp_base.col_size = 5
bp_base.row_size = 8
bp_base.max_columns = 2
bp_base.max_rows = 2
bp_base.passes_count = 3000
bp_base.tile_styles = [
    custom_item,    
    custom_item_rotated_y_pos,
    custom_item_rotated_y_neg
]

bp_base.make()

ex_base = bp_base.build()
#show_object(ex_base)

cq.exporters.export(ex_base, "stl/minibase_ruin_stone_base.stl")
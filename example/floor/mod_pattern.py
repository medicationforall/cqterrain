import cadquery as cq
from cqterrain.floor import ModPattern

bp_hex = ModPattern()
bp_hex.x_spacing = [5,10]
bp_hex.y_spacing = [5]
bp_hex.row_x_mod = [0,1]
bp_hex.row_x_offset = [0,-2.5]

bp_hex.x_stretch = 1
bp_hex.y_stretch = 1

bp_hex.taper = 10
bp_hex.offset = -.25
bp_hex.render_points = False

bp_hex.debug = False
bp_hex.column_pad = 1
bp_hex.row_pad = 0
bp_hex.grid_offset_x = -1.25 - 4
bp_hex.grid_offset_y = 0

bp_hex.make()

ex_hex_outline = bp_hex.build_outline()
ex_hex = bp_hex.build()

#show_object(ex_hex)

cq.exporters.export(ex_hex,'stl/floor_mod_pattern.stl')
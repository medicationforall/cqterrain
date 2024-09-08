import cadquery as cq
from cqterrain.bridge import TileStraight
from cqterrain.tile import plain

bp_straight = TileStraight()

bp_straight.length = 75*2
bp_straight.width = 75*2
bp_straight.height = 50

bp_straight.padding = 4
bp_straight.tile_height = 4
bp_straight.tile_length = 26
bp_straight.tile_width = 18
bp_straight.tile_padding = 1
bp_straight.tile_method = plain

bp_straight.base_top_margin = 10
bp_straight.base_side_margin = 10
bp_straight.base_fillet = 8

bp_straight.base_inset_distance_height = 2
bp_straight.base_inset_distance = 2
bp_straight.base_inset_depth = 2
bp_straight.base_inset_fillet = 9

bp_straight.render_tile = True

bp_straight.make()

ex_straight = bp_straight.build()

#show_object(ex_straight)
cq.exporters.export(ex_straight,'stl/bridge_tile_straight.stl')
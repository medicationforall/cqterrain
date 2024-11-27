import cadquery as cq
from cqterrain.walkway import Walkway

from cqterrain import tile

def custom_tile(length, width, height):
    c_tile = tile.rivet(
    length = length,
    width = width,
    height = height,
    padding = 1,
    internal_padding = height + .5,
    rivet_height = 0.5,
    rivet_radius = .5
)
    return c_tile

bp = Walkway()
bp.length = 225
bp.width = 75
bp.height = 6

bp.walkway_chamfer = 3

bp.render_slots = 'grid'
bp.make_tile_method = custom_tile
bp.tile_length= 20
bp.tile_length= 15

bp.render_tabs = True
bp.tab_chamfer = 4.5
bp.tab_height = 2
bp.tab_length = 5

bp.render_rails = True
bp.rail_width = 4
bp.rail_height = 40
bp.rail_chamfer = 28

bp.render_rail_slots = True
bp.rail_slot_length = 10
bp.rail_slot_top_padding = 6
bp.rail_slot_length_offset = 12
bp.rail_slots_end_margin = 15
bp.rail_slot_pointed_inner_height = 7
bp.rail_slot_type = 'archpointed'

bp.make()
walkway_bridge = bp.build()

#show_object(walkway_bridge)

cq.exporters.export(walkway_bridge, 'stl/walkway_tiled_bridge.stl')
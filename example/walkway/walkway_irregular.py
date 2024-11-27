import random
import cadquery as cq
from cqterrain.walkway import Walkway
from cqterrain import tile as terrain_tile, greeble

def __vent_greeble(length, width, height):
    t = greeble.vent(length, width, height ,inner_width = height-1,)
    return t

tile_styles = [
    terrain_tile.plain,
    terrain_tile.chamfer_frame,
    terrain_tile.rivet,
    terrain_tile.slot,
    __vent_greeble
]

tile_styles_count = len(tile_styles)

def custom_tile(length, width, height):
    tile_style = random.randrange(0,4)

    if tile_style in range(tile_styles_count):
        tile = tile_styles[tile_style](length, width, height)
    else:
        raise Exception(f"unknown tyle style {tile_style}")
    return tile

def custom_tile2(length, width, height):
    tile_style = random.randrange(0,5)

    if tile_style in range(tile_styles_count):
        tile = tile_styles[tile_style](length, width, height)
    else:
        raise Exception(f"unknown tyle style {tile_style}")
    return tile

bp = Walkway()
bp.length = 225
bp.width = 75
bp.height = 6

bp.walkway_chamfer = 3

bp.render_slots = 'irregular'
bp.tile_max_height = 4
bp.tile_seed = 'ork12'
bp.make_tile_method = custom_tile2
bp.tile_max_columns = 6
bp.tile_max_rows = 6

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

cq.exporters.export(walkway_bridge, 'stl/walkway_ireg_bridge.stl')

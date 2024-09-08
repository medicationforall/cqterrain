import cadquery as cq
from cqterrain.bridge import TileBridge
from cqterrain.tile import bolt_panel


bp_bridge = TileBridge()
bp_bridge.height = 50
bp_bridge.straight_count = 3
bp_bridge.bp_straight.tile_height = 3
bp_bridge.bp_straight.tile_padding = 1
bp_bridge.bp_straight.tile_method = bolt_panel #type:ignore
bp_bridge.make()
ex_bridge = bp_bridge.build()

#show_object(ex_bridge)
cq.exporters.export(ex_bridge,'stl/bridge_tile.stl')
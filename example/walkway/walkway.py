import cadquery as cq
from cqterrain.walkway import Walkway

bp = Walkway()
bp.length = 225
bp.width = 75
bp.height = 6

bp.walkway_chamfer = 3

bp.render_slots = True
bp.slot_length = 3
bp.slot_width_padding = 5
bp.slot_length_offset = 5
bp.slot_width_padding = 4
bp.slots_end_margin = 0

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

bp.length = 150
bp.width = 50
bp.slot_length = 2.5
bp.slot_length_offset = 3.5
bp.slot_width_padding = 2
bp.rail_height = 20
bp.rail_chamfer = 10
bp.rail_slot_length = 6
bp.rail_slot_length_offset = 4
bp.rail_slots_end_margin = 8
bp.rail_slot_type = 'box'
bp.make()
walkway = bp.build()

mini_proxy = (
    cq.Workplane("XY")
    .cylinder(32,12.5)
)


#show_object(walkway_bridge)
#show_object(walkway.translate((0,-80,0)))

cq.exporters.export(walkway_bridge, 'stl/walkway_bridge.stl')
cq.exporters.export(walkway, 'stl/walkway.stl')

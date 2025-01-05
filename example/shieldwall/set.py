import cadquery as cq
from cqterrain.shieldwall import Set

set_bp = Set()

set_bp.straight_count = 4
set_bp.padding = 5
set_bp.height = 25

set_bp.base_height = 5.6
set_bp.magnet_padding_x = 2

set_bp.corner_count = 2

set_bp.end_cap_count = 4
set_bp.end_cap_length = 15

set_bp.make()
set_ex = set_bp.build()

#show_object(set_ex)
cq.exporters.export(set_ex, 'stl/shieldwall_set.stl')
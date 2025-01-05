import cadquery as cq
from cqterrain.shieldwall import StraightBasic

straight_bp = StraightBasic()

straight_bp.length = 75
straight_bp.width = 20
straight_bp.height = 20
straight_bp.base_height = 5.6
straight_bp.render_magnets = True
straight_bp.magnet_padding = 1
straight_bp.magnet_padding_x = 2

straight_bp.make()
straight_ex = straight_bp.build()

#show_object(straight_ex)
cq.exporters.export(straight_ex, 'stl/shieldwall_straight_basic.stl')
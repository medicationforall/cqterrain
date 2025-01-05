import cadquery as cq
from cqterrain.shieldwall import HexStraight

hex_bp = HexStraight()
hex_bp.length = 75
hex_bp.width = 20
hex_bp.height = 25
hex_bp.base_height = 5.6
hex_bp.render_magnets = True
hex_bp.magnet_padding = 1
hex_bp.magnet_padding_x = 2
hex_bp.cut_padding_x = 3
hex_bp.cut_padding_z = 3
hex_bp.post_length = 2
hex_bp.post_padding_y = 1
hex_bp.cut_width = .8
hex_bp.key_margin = 0.2
hex_bp.render_base_cut = True
hex_bp.base_cut_height = None
hex_bp.base_cut_width = None
hex_bp.mesh_width = 4
hex_bp.make()

result = hex_bp.build()

#show_object(result)
cq.exporters.export(result, 'stl/shieldwall_hex_straight.stl')
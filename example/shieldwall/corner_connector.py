import cadquery as cq
from cqterrain.shieldwall import CornerConnector

corner_bp = CornerConnector()
corner_bp.length = 20
corner_bp.width = 20
corner_bp.height = 25

corner_bp.base_height = 5.6

corner_bp.render_magnets = True
corner_bp.magnet_padding = 1
corner_bp.magnet_padding_x = 2

corner_bp.side_margin = -2
corner_bp.side_height = 1
corner_bp.top_height = 2

corner_bp.cut_width = 3
corner_bp.middle_width_inset = -6

corner_bp.render_greeble = True
corner_bp.greeble_padding_y = 1

corner_bp.make()
corner_ex = corner_bp.build()
corner_ex_assembly = corner_bp.build_assembly()

#show_object(corner_ex)
cq.exporters.export(corner_ex, 'stl/shieldwall_corner_connector.stl')
corner_ex_assembly.export("gltf/shieldwall_corner_connector.gltf")
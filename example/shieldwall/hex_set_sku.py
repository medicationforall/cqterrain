import cadquery as cq
from cqterrain.shieldwall import HexSet

hex_set_bp = HexSet()
hex_set_bp.base_height = 5.6

hex_set_bp.straight_count = 1
hex_set_bp.corner_count = 1
hex_set_bp.end_cap_count = 1

hex_set_bp.make()
hex_set = hex_set_bp.build()

straight_wall_bp = hex_set_bp.straight_bp
key = straight_wall_bp.key_template

scene = hex_set.add(key.translate((-75,0,-12.5+1)))

cq.exporters.export(scene, 'stl/shieldwall_hex_sku.stl')
import cadquery as cq
from cqterrain.shieldwall import Straight

straight_bp = Straight()
straight_bp.length = 75
straight_bp.width = 20
straight_bp.height = 25

straight_bp.mesh_width = 4

straight_bp.mesh_bp.tile_length =10
straight_bp.mesh_bp.tile_width = 5
straight_bp.mesh_bp.tile_padding = 0.3
straight_bp.mesh_bp.tile_chamfer = 1
straight_bp.make()
straight_ex = straight_bp.build()

cross_section = cq.Workplane('XY').box(10,straight_bp.width,50)

#show_object(straight_ex.cut(cross_section))
#show_object(straight_ex)

cq.exporters.export(straight_ex.cut(cross_section), 'stl/shieldwall_straight_demo.stl')
cq.exporters.export(straight_bp.key_template, 'stl/shieldwall_straight_key.stl')
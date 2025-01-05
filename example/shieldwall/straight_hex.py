import cadquery as cq
from cqterrain.shieldwall import Straight, HexMesh

straight_bp = Straight()
straight_bp.length = 75
straight_bp.width = 20
straight_bp.height = 25

straight_bp.shape_bp.base_height = 7

straight_bp.mesh_width = 4

straight_bp.mesh_bp = HexMesh() 
straight_bp.mesh_bp.tile_length =10
straight_bp.mesh_bp.tile_width = 10
straight_bp.mesh_bp.tile_padding = 0.0
straight_bp.mesh_bp.tile_chamfer = 1
straight_bp.make()
straight_ex = straight_bp.build()

cross_section = cq.Workplane('XY').box(10,straight_bp.width,50)

straight_ex_assembly = straight_bp.build_assembly()

#show_object(straight_ex)
cq.exporters.export(straight_ex, 'stl/shieldwall_straight_hex.stl')
straight_ex_assembly.save("gltf/shieldwall_straight_hex.gltf")



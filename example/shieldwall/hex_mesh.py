import cadquery as cq
from cqterrain.shieldwall import HexMesh

mesh_bp = HexMesh()
mesh_bp.height = 50
mesh_bp.tile_length =10
mesh_bp.tile_width = 10
mesh_bp.tile_padding = .0
mesh_bp.tile_chamfer = 0.5
mesh_bp.make()
mesh_ex = mesh_bp.build()

#show_object(mesh_ex)
cq.exporters.export(mesh_ex, 'stl/shieldwall_hex_mesh.stl')

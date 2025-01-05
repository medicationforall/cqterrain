import cadquery as cq
from cqterrain.shieldwall import Mesh

mesh_bp = Mesh()

mesh_bp.length = 75
mesh_bp.width = 3
mesh_bp.height = 25

mesh_bp.tile_length = 5
mesh_bp.tile_width = 5
mesh_bp.tile_padding = 0.2
mesh_bp.tile_chamfer = 1.4

mesh_bp.make()
mesh_ex = mesh_bp.build()

#show_object(mesh_ex)
cq.exporters.export(mesh_ex, 'stl/shieldwall_mesh.stl')
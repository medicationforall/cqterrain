import cadquery as cq
from cqterrain.shieldwall import GothicMesh

gothic_bp = GothicMesh()
gothic_bp.length = 75
gothic_bp.width = 3
gothic_bp.height = 25
gothic_bp.tile_width = 5
gothic_bp.tile_chamfer = 1.4
gothic_bp.tile_length = 10
gothic_bp.tile_padding = 0
gothic_bp.arch_frame_width = 1.5
gothic_bp.side_length = None

gothic_bp.make()
gothic_ex = gothic_bp.build()

#show_object(gothic_ex)
cq.exporters.export(gothic_ex, 'stl/shieldwall_gothic_mesh.stl')
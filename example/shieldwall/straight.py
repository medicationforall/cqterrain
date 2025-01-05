import cadquery as cq
from cqterrain.shieldwall import Straight, HexMesh

straight_bp = Straight()
straight_bp.length = 75
straight_bp.width = 20
straight_bp.height = 25

straight_bp.base_height = 5.6

straight_bp.render_magnets = True
straight_bp.magnet_padding= 1
straight_bp.magnet_padding_x = 2

straight_bp.cut_padding_x = 3
straight_bp.cut_padding_z = 3

straight_bp.post_length= 2
straight_bp.post_padding_y = 1
straight_bp.mesh_width = 3

straight_bp.cut_width= .8
straight_bp.key_margin = 0.2

straight_bp.render_base_cut= True
straight_bp.base_cut_height = None
straight_bp.base_cut_width= None

straight_bp.make()
straight_ex = straight_bp.build()

key = straight_bp.key_template

#show_object(straight_ex)
cq.exporters.export(straight_ex, 'stl/shieldwall_straight.stl')
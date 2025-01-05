import cadquery as cq
from cqterrain.shieldwall import CurveBasic, ShieldShape, Magnets


wall_bp = CurveBasic()
wall_bp.width = 20
wall_bp.height = 25
wall_bp.base_height = 5.6

wall_bp.x_radius = 75
wall_bp.y_radius = 75 #ellipse stretch
wall_bp.angle = 270
wall_bp.rotation_angle = 0

wall_bp.render_magnets = True
wall_bp.magnet_padding = 1
wall_bp.magnet_padding_x = 2

# blueprints
wall_bp.shape_bp = ShieldShape()
wall_bp.magnets_bp = Magnets()


wall_bp.make()
wall_ex = wall_bp.build()

#show_object(wall_ex)
cq.exporters.export(wall_ex, 'stl/shieldwall_curve_basic.stl')
import cadquery as cq
from cqterrain.shieldwall import CurveBasic, ArchShape


wall_bp = CurveBasic()
wall_bp.shape_bp = ArchShape()

#90 degrees
wall_bp.angle = 270
wall_bp.rotation_angle=0

#45 degrees
#wall_bp.angle = 315
#wall_bp.rotation_angle=-45

#60 degrees
#wall_bp.angle = 300
#wall_bp.rotation_angle=-30


wall_bp.make()
wall_ex = wall_bp.build()

#show_object(wall_ex)
cq.exporters.export(wall_ex, 'stl/shieldwall_curve_basic_arch.stl')
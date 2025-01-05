import cadquery as cq
from cqterrain.shieldwall import Magnets

magnet_bp = Magnets()

magnet_bp.distance = 12.9
magnet_bp.pip_height = 2.4
magnet_bp.pip_radius = 1.56

magnet_bp.make()
magnet_ex = magnet_bp.build()

#show_object(magnet_ex)
cq.exporters.export(magnet_ex,'stl/shieldwall_magnets.stl')
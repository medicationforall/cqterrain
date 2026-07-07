import cadquery as cq
from cqterrain.wall import BaseWall

bp = BaseWall()
bp.length = 75
bp.width = 4
bp.height = 75
bp.make()

ex_wall = bp.build()
#show_object(ex_wall)

cq.exporters.export(ex_wall, 'stl/wall_base_wall.stl')

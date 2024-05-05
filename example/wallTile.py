import cadquery as cq
from cqterrain import Wall
from cadqueryhelper import shape

cylinder = shape.cylinder(10, 5)
star = shape.star()

bb = Wall(inside_tile=cylinder, outside_tile=star, height=75)
bb.make()
part = bb.build()
workspace = cq.Workplane('XY')
workspace.add(part)

cq.exporters.export(workspace,'stl/wallTile.stl')

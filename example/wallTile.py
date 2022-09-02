import cadquery as cq
from cqterrain import tile_wall
from cadqueryhelper import shape

cylinder = shape.cylinder(10, 5)
star = shape.star()

part = tile_wall(inside_tile=cylinder, outside_tile=star, height=75)
workspace = cq.Workplane('XY')
workspace.add(part)

cq.exporters.export(workspace,'out/wallTile.stl')

if part.metadata:
    print(part.metadata)

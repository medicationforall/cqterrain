import cadquery as cq
from cqterrain import Wall

bb = Wall()
bb.make()
wall = bb.build()
workspace = cq.Workplane('XY')
workspace.add(wall)

cq.exporters.export(workspace,'out/wall.stl')

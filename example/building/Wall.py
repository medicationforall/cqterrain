import cadquery as cq
from cqterrain.building import Wall

bb = Wall()
bb.make()
wall = bb.build()
workspace = cq.Workplane('XY')
workspace.add(wall)

cq.exporters.export(workspace,'stl/wall.stl')

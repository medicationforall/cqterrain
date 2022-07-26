import cadquery as cq
from cqterrain import wall

part = wall.make_wall()
workspace = cq.Workplane('XY')
workspace.add(part)

cq.exporters.export(workspace,'out/wall.stl')

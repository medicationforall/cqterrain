import cadquery as cq
from cqterrain import wall

part = wall()
workspace = cq.Workplane('XY')
workspace.add(part)

cq.exporters.export(workspace,'out/wall.stl')

import cadquery as cq
from cqterrain import support

part = support()
workspace = cq.Workplane('XY')
workspace.add(part)

cq.exporters.export(workspace,'stl/support.stl')

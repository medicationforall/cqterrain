import cadquery as cq
from cqterrain import floor

f = floor.make_floor()
workspace = cq.Workplane('XY')
workspace.add(f)

cq.exporters.export(workspace,'out/floor.stl')

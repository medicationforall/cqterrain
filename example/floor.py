import cadquery as cq
from cqterrain import Floor

bp = Floor()
bp.make()
f = bp.build()
workspace = cq.Workplane('XY')
workspace.add(f)

cq.exporters.export(workspace,'out/floor.stl')

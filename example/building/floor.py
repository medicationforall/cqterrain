import cadquery as cq
from cqterrain.building import Floor

bp = Floor()
bp.make()
f = bp.build()
workspace = cq.Workplane('XY')
workspace.add(f)

cq.exporters.export(workspace,'stl/floor.stl')
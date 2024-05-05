import cadquery as cq
from cqterrain import Floor
from cadqueryhelper import shape

cone = shape.cone()
cube = shape.cube()
cylinder = shape.cylinder(12, 20)

bp = Floor(tile=cylinder, width=200)
bp.make()
f = bp.build()
workspace = cq.Workplane('XY')
workspace.add(f)

print('create floorTile.stl')
cq.exporters.export(workspace,'stl/floorTile.stl')

#if f.metadata:
#    print(f.metadata)

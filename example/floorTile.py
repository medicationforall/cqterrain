import cadquery as cq
from cqterrain import floor
from cadqueryhelper import shape

cone = shape.cone()
cube = shape.cube()
cylinder = shape.cylinder(12, 20)

f = floor.make_tile_floor(cylinder, width=200)
workspace = cq.Workplane('XY')
workspace.add(f)

print('create floorTile.stl')
cq.exporters.export(workspace,'out/floorTile.stl')

if f.metadata:
    print(f.metadata)

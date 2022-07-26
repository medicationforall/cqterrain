import cadquery as cq
from cqterrain import floor
from cadqueryhelper import shape

cone = shape.cone()
cube = shape.cube()
cylinder = shape.cylinder(10, 20)

f = floor.make_tile_floor(cylinder)
workspace = cq.Workplane('XY')
workspace.add(f)

print('create floorTile.stl')
cq.exporters.export(workspace,'out/floorTile.stl')

if f.metadata:
    print(f.metadata)

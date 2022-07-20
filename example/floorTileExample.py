import cadquery as cq
from cqterrain import floor
from cadqueryhelper import parts

cone = parts.make_cone()
cube = parts.make_cube()
cylinder = parts.make_cylinder(10, 10)

f = floor.make_tile_floor(cylinder)
workspace = cq.Workplane('XY')
workspace.add(f)

print('create floorTile.stl')
cq.exporters.export(workspace,'out/floorTile.stl')

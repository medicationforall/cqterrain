import cadquery as cq
from cqterrain import floor
from cadqueryhelper import parts

cone = parts.make_cone()
cube = parts.make_cube()

f = floor.make_tile_floor(cube)
workspace = cq.Workplane('XY')
workspace.add(f)

cq.exporters.export(workspace,'out/floorTile.stl')

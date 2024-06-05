import cadquery as cq
from cqterrain.building import Floor
from cadqueryhelper import shape

cone = shape.cone()
cube = cq.Workplane("XY").box(5,5,5)
cylinder = cq.Workplane("XY").cylinder(20, 12)

bp_floor = Floor(tile=cylinder, width=200)
bp_floor.length = 100 
bp_floor.width = 100
bp_floor.height = 3 
bp_floor.tile = cylinder 
bp_floor.tile_padding = 0

bp_floor.make()
result = bp_floor.build()

#show_object(floor_ex)
cq.exporters.export(result,'stl/building_floorTile.stl')



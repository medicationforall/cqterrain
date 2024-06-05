import cadquery as cq
from cqterrain.building import Wall
from cadqueryhelper import shape

cylinder = cq.Workplane("XY").cylinder(5, 10)
star = shape.star()

bp_wall = Wall()
bp_wall.length = 100
bp_wall.width = 3
bp_wall.height = 75
bp_wall.inside_tile = cylinder
bp_wall.outside_tile = star

bp_wall.make()
result = bp_wall.build()

#show_object(result)
cq.exporters.export(result,'stl/building_wall_tile.stl')

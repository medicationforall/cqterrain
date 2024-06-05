import cadquery as cq
from cqterrain.building import Wall
from cadqueryhelper import shape

bp_wall = Wall()
bp_wall.length = 100
bp_wall.width = 3
bp_wall.height = 50
bp_wall.inside_tile = None
bp_wall.outside_tile = None

bp_wall.make()
result = bp_wall.build()

#show_object(result)
cq.exporters.export(result,'stl/building_wall.stl')

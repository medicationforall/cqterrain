import cadquery as cq
from cqterrain.building import Floor

bp_floor = Floor()
bp_floor.length = 100 
bp_floor.width = 100
bp_floor.height = 3 
bp_floor.tile = None 
bp_floor.tile_padding = 0

bp_floor.make()
result = bp_floor.build()

#show_object(floor_ex)
cq.exporters.export(result,'stl/building_floor.stl')

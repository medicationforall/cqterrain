import cadquery as cq
from  cqterrain.building  import Room

bp_room = Room()
bp_room.length= 120
bp_room.width = 80
bp_room.height= 50
bp_room.wall_width = 3
bp_room.floor_height = 3
bp_room.floor_padding = 0
bp_room.floor_tile = None
bp_room.floor_tile_padding = 0
bp_room.style = "office"
bp_room.window_count= 1
bp_room.door_walls = [False, True, False, False]
bp_room.window_walls = [True, False, True, True]
bp_room.build_walls = [True, True, True, True]

bp_room.make()
result = bp_room.build()

#show_object(result)
cq.exporters.export(result,'stl/building_room.stl')

import cadquery as cq
from cadqueryhelper import grid
from cqterrain.building import Floor, Room
from cqterrain import tile

combined = tile.octagon_with_dots()
#combined = tile.basketweave()

bp = Floor()
bp.tile = combined
bp.tile_padding = .5
bp.make()

floor = bp.build()

bp_room = Room(width=120,floor_padding = 4, window_count=6)
bp_room.make()

# add tile to room floor
bp_room_floor = bp_room.floor
bp_room_floor.tile = combined
bp_room_floor.tile_padding = .5
bp_room_floor.make()

room = bp_room.build()


#show_object(room)
cq.exporters.export(room,'stl/room_with_tile.stl')

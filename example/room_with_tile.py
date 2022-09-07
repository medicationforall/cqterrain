import cadquery as cq
from cadqueryhelper import grid
from cqterrain import Floor, Room

#def tile_pattern_one():

tile = (cq.Workplane("XY")
        .rect(5,5)
        .extrude(1)
        .edges("|Z")
        .chamfer(1.2) # SET PERCENTAGE
        )

rotated_tile = tile.rotate((0,0,1),(0,0,0), 45)

mid_tile = (cq.Workplane("XY")
        .rect(1.6,1.6)
        .extrude(1)
        .rotate((0,0,1),(0,0,0), 45)
        )


tiles = grid.make_grid(tile, [5.5,5.5], rows=3, columns=3)
center_tiles = grid.make_grid(mid_tile, [5.5,5.5], rows=4, columns=4)

combined = tiles.add(center_tiles).translate((0,0,-1*(1/2)))

bp = Floor()
bp.tile = combined
bp.tile_padding = .5
bp.make()

floor = bp.build()

bp_room = Room(width=120, floor_padding = 4,  window_count=6)
bp_room.make()

# add tile to room floor
bp_room_floor = bp_room.floor
bp_room_floor.tile = combined
bp_room_floor.tile_padding = .5
bp_room_floor.make()

room = bp_room.build()

#show_object(tiles)
#show_object(combined)

#show_object(floor)
#show_object(room)

#show_object(mid_tile)
#show_object(rotated_tile)

cq.exporters.export(room,'out/room_with_tile.stl')

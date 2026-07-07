import cadquery as cq
from cqterrain.floor import TileFloor
from cqterrain import tile

bp_floor = TileFloor()

bp_floor.length = 100
bp_floor.width = 50
bp_floor.height = 4

bp_floor.tile_length = 25
bp_floor.tile_width = 25
bp_floor.tile_method = tile.bolt_panel #Callable[[float,float,float],cq.Workplane]
bp_floor.count_overflow = (0,0) #tuple[int,int]
bp_floor.tile_spacing = (.5,.5) #tuple[float,float]

bp_floor.make()
ex_floor = bp_floor.build()
ex_outline = bp_floor.build_outline()

#show_object(ex_floor)
#show_object(ex_outline)
cq.exporters.export(ex_floor,'stl/floor_tile_floor.stl')
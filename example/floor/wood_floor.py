import cadquery as cq
from cqterrain.floor import WoodFloor

bp_floor = WoodFloor()
bp_floor.board_width = 5
bp_floor.render_joists = False
bp_floor.make()

ex_floor = bp_floor.build()

#show_object(ex_floor)
cq.exporters.export(ex_floor,'stl/floor_woodfloor.stl')
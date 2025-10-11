import cadquery as cq
from cqterrain.floor import WoodFloor

bp_floor = WoodFloor()
bp_floor.length= 150
bp_floor.width= 75
bp_floor.height = 8

#joist
bp_floor.joist_width = 3
bp_floor.joist_space = 12.5
bp_floor.joist_count= 7
bp_floor.render_joists= True

# Board
bp_floor.board_width= 5
bp_floor.board_width_spacer = .1
bp_floor.board_height = 1.5

#nail
bp_floor.nail_diameter = .4
bp_floor.nail_overlap_height = .2
bp_floor.nail_x_margin = .5
bp_floor.nail_y_margin = .5

# grid
bp_floor.seed= "redd2"
bp_floor.board_lengths = [1,4]
bp_floor.board_break_width= .2
bp_floor.grid = []

bp_floor.make()

ex_floor = bp_floor.build()

#show_object(ex_floor)
cq.exporters.export(ex_floor,'stl/floor_woodfloor_struct.stl')
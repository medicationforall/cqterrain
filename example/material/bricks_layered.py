import cadquery as cq
from cqterrain.material import BricksLayered

bp_bricks = BricksLayered()
bp_bricks.length = 30
bp_bricks.width = 25
bp_bricks.height = 60
bp_bricks.rows = 4
bp_bricks.columns = 3
bp_bricks.layers = 5
bp_bricks.spacing = .7
bp_bricks.spacing_z = 0
bp_bricks.tile_padding = 2
bp_bricks.make()

ex_bricks = bp_bricks.build()

#show_object(ex_bricks)
cq.exporters.export(ex_bricks,'stl/material_bricks_layered.stl')
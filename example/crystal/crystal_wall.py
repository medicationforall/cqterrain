import cadquery as cq
from cqterrain.crystal import CrystalWall

bp_wall = CrystalWall()
bp_wall.length = 75
bp_wall.height = (20,40,2.5)
bp_wall.width = 30
bp_wall.render_base = True
bp_wall.render_crystals = True
bp_wall.crystal_margin = 10
bp_wall.crystal_count = 10
bp_wall.seed = "zoe"
bp_wall.random_rotate_x = (-20.0, 20.0, 2.5)
bp_wall.random_rotate_y = (-15.0, 15.0, 2.5)
#bp_wall.random_rotate_x = 30
#bp_wall.random_rotate_y = None
bp_wall.make()

ex_wall = bp_wall.build()

#show_object(ex_wall)
cq.exporters.export(ex_wall,'stl/crystal_wall.stl')
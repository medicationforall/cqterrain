import cadquery as cq
from cqterrain.crystal import CrystalWall

bp_wall = CrystalWall()
bp_wall.length = 75
bp_wall.height = (20,40,2.5)
bp_wall.width = 30
bp_wall.render_base = True
bp_wall.base_height = 3
bp_wall.base_taper = -1
bp_wall.base_render_magnet = False
bp_wall.base_detail_height = 3
bp_wall.base_uneven_height= 4
bp_wall.base_peak_count = (9,10)
bp_wall.base_segments = 6
bp_wall.render_crystals = True
bp_wall.crystal_base_width = 20.0
bp_wall.crystal_base_height = 0.5
bp_wall.crystal_inset_width = 20.0
bp_wall.crystal_inset_height = (1.0,3.0,0.5)
bp_wall.crystal_mid_height = (2.0,5.0,0.5)
bp_wall.crystal_mid_width = (10,20.0,2.5)
bp_wall.crystal_top_height = (10,15,2.5)
bp_wall.crystal_top_width = (10,15.0,2.5)
bp_wall.crystal_faces = (5,10,1)
bp_wall.crystal_intersect = True
bp_wall.crystal_margin = 10
bp_wall.crystal_count = 10
bp_wall.seed = "zoe"
bp_wall.random_rotate_x = (-20.0, 20.0, 2.5)
bp_wall.random_rotate_y = (-15.0, 15.0, 2.5)
#bp_wall.random_rotate_x = 30
#bp_wall.random_rotate_y = None
bp_wall.make()

ex_plate = bp_wall.build_plate()
cq.exporters.export(ex_plate,'stl/crystal_wall_plate.stl')
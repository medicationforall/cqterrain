import cadquery as cq
from cqterrain import window

lattice = window.lattice(
    length = 20, 
    height = 40,  
    tile_size = 4, 
    lattice_width = 1, 
    lattice_height = 1, 
    lattice_angle = 45
)
frame = window.frame()

scene = cq.Workplane("XY").add(frame).add(lattice)

cq.exporters.export(scene,'stl/window_lattice.stl')

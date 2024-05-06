import cadquery as cq
from cqterrain import window

#grill = window.grill(height=40, columns=2)
lattice = window.lattice(lattice_angle=20, tile_size=6)
frame = window.frame()

#show_object(lattice)
#show_object(frame)

scene = cq.Workplane("XY").add(frame).add(lattice)

cq.exporters.export(scene,'stl/window_lattice.stl')

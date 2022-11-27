import cadquery as cq
from cqterrain import window

case_win = window.cinquefoil_frame(outer_radius=7.5, radius=5, sides=5, inner_radius=3, height=2)
scene = cq.Workplane("XY").add(case_win)

cq.exporters.export(scene,'out/window_cinquefoil.stl')

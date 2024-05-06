import cadquery as cq
from cqterrain import window

case_win = window.casement(length=20, width=4, height=40, colums=2, rows=3, frame_width=2, grill_width=1, grill_height=1)
scene = cq.Workplane("XY").add(case_win)

cq.exporters.export(scene,'stl/window_casement.stl')

import cadquery as cq
from cqterrain import window

case_win = window.grill(length=20, width=4, height=40, columns=4, rows=2, grill_width=1, grill_height=1)
scene = cq.Workplane("XY").add(case_win)

cq.exporters.export(scene,'out/window_grill.stl')

import cadquery as cq
from cqterrain import window

result = window.casement(
    length=20, 
    width=4, 
    height=40, 
    colums=2, 
    rows=3, 
    frame_width=2, 
    grill_width=1, 
    grill_height=1
)

cq.exporters.export(result,'stl/window_casement.stl')

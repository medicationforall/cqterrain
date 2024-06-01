import cadquery as cq
from cqterrain import window

result = window.grill(
    length=20, 
    height=40, 
    columns=4, 
    rows=2, 
    grill_width=1, 
    grill_height=1
)

cq.exporters.export(result,'stl/window_grill.stl')

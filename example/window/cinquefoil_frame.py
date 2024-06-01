import cadquery as cq
from cqterrain import window

result = window.cinquefoil_frame(
    outer_radius=7.5, 
    radius=5, 
    sides=5, 
    inner_radius=3, 
    height=2
)

cq.exporters.export(result,'stl/window_cinquefoil_frame.stl')

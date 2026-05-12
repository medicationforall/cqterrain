import cadquery as cq
from cqterrain import window

result = window.cinquefoil(
    radius = 5, 
    sides = 5, 
    inner_radius = 3, 
    height = 2
)

#show_object(result)
cq.exporters.export(result,'stl/window_cinquefoil.stl')
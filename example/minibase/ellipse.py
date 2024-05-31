import cadquery as cq
from cqterrain.minibase import ellipse

result = ellipse(
    x_diameter=52, 
    y_diameter=90, 
    height=3, 
    taper=-1,
    render_magnet = True,  
    magnet_diameter=3, 
    magnet_height=2
)

#show_object(result)
cq.exporters.export(result,'stl/minibase_ellipse.stl')
import cadquery as cq
from cqterrain.minibase import hexagon

result = hexagon(
    diameter = 25,
    height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2
)

#show_object(result)
cq.exporters.export(result,'stl/minibase_hexagon.stl')
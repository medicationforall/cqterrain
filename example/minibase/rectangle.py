import cadquery as cq
from cqterrain.minibase import rectangle

result = rectangle(
    length = 25, 
    width = 25, 
    height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2
)

#show_object(result)
cq.exporters.export(result,'stl/minibase_rectangle.stl')
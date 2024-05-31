import cadquery as cq
from cqterrain.minibase import slot

result = slot(
    length = 24, 
    width = 50, 
    height = 3, 
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2
)

#show_object(result)
cq.exporters.export(result,'stl/minibase_slot.stl')
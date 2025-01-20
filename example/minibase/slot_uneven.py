import cadquery as cq
from cqterrain.minibase import slot_uneven

ex_base = slot_uneven(
    length = 75,
    width = 25,
    base_height = 3,
    taper = -1,
    render_magnet = True,  
    magnet_diameter = 3, 
    magnet_height = 2,
    detail_height = 3,
    uneven_height = 4,
    peak_count = (9,10),
    segments = 6,
    seed="red"
)

#show_object(ex_base)
cq.exporters.export(ex_base,'stl/minibase_slot_uneven.stl')
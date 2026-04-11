import cadquery as cq
from cqterrain.greeble import cap_greeble

result = cap_greeble(
    diameter = 28, 
    teeth = 14,
    rotate_teeth = 20,
    body_height = 3,
    teeth_diameter = 3,
    chamfer = 2,
    interior_height = 2,
    interior_diameter = 4,
    interior_cut_diameter = 5,
    bars_count = 6,
    bar_length = 6,
    bar_diameter = 2,
    inset_distance = 2,
    bar_shift = 1,
    bar_shift_z = 2.4
)

#show_object(result)
cq.exporters.export(result, 'stl/greeble_cap_greeble.stl')
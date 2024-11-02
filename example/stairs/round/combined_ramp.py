import cadquery as cq
from cqterrain.stairs.round import ramp

round_ramp = ramp(
    stair_count = 12*2,
    height = 75,
    inner_diameter = 75,
    diameter = 75 + 55,
    distance_overlap = 0.5,
    debug = False
).translate((0,0,(75)/2))

cut_ramp = ramp(
    stair_count = 12*2,
    height = 75,
    inner_diameter = 75,
    diameter = 75 + 55,
    distance_overlap = 0.5,
    debug = False
).translate((0,0,(75)/2))

round_ramp = round_ramp.rotate((0,0,1),(0,0,0),7) 

combined_ramp = round_ramp.cut(cut_ramp)

# show_object(combined_ramp)

cq.exporters.export(combined_ramp,'stl/stairs_round_combined_ramp.stl')
import cadquery as cq
from cqterrain.stairs.round import ramp, plain_stairs

stairs = plain_stairs(
    stair_count = 12,
    height = 75,
    inner_diameter = 75,
    diameter = 75 + 55, 
    debug = False
).translate((0,0,(75)/2))

round_ramp = ramp(
    stair_count = 12*2,
    height = 75,
    inner_diameter = 75,
    diameter = 75 + 55,
    distance_overlap = 0.5,
    debug = False
).translate((0,0,(75)/2))

stairs = stairs.rotate((0,0,1),(0,0,0),7) 

combined_stairs = stairs.cut(round_ramp)

#show_object(combined_stairs)

cq.exporters.export(combined_stairs,'stl/stairs_round_combined_plain.stl')
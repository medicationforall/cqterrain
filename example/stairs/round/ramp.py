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

# show_object(round_ramp)


cq.exporters.export(round_ramp,'stl/stairs_round_ramp.stl')
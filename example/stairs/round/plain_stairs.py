import cadquery as cq
from cqterrain.stairs.round import plain_stairs

stairs = plain_stairs(
    stair_count = 12,
    height = 75,
    inner_diameter = 75,
    diameter = 75 + 55, 
    debug = False
).translate((0,0,(75)/2))

#show_object(stairs)

cq.exporters.export(stairs,'stl/stairs_round_plain_stairs.stl')
import cadquery as cq
from cqterrain.ruin import ruin_corner_random

result = ruin_corner_random(
    length = 50, 
    width = 50, 
    height = 10, 
    points = 7,
    debug = False,
    shift = (-4,5,1),
    seed = "pokey"
)

#show_object(result)
cq.exporters.export(result,"stl/ruin_corner_random.stl")
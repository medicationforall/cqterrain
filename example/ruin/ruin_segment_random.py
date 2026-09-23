import cadquery as cq
from cqterrain.ruin import ruin_segment_random

result = ruin_segment_random(
    length = 75, 
    width = 50, 
    height = 10, 
    points = (7,7,7),
    debug = False,
    shift = (-2,4,1),
    seed = "test"
)

#show_object(result)
cq.exporters.export(result, 'stl/ruin_segment_random.stl')

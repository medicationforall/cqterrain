import cadquery as cq
from cqterrain.ruin import ruin_rectangle_random

ex_ruin = ruin_rectangle_random(
    length = 125, 
    width = 10, 
    height = 4,
    points = 12,
    debug=False,
    shift = (-1,2,1),
    seed = "test"
)

#show_object(ex_ruin)

cq.exporters.export(ex_ruin, 'stl/ruin_rectangle_random.stl')
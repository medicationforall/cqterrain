import cadquery as cq
from cqterrain.ruin import ruin_corner

result = ruin_corner(
    length = 50, 
    width = 50, 
    height = 10, 
    points = 7,
    adjustments = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
    debug = False
)

#show_object(result)
cq.exporters.export(result, 'stl/ruin_ruin_corner.stl')
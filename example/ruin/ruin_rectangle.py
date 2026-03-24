import cadquery as cq
from cqterrain.ruin import ruin_rectangle

ex_ruin = ruin_rectangle(
    length = 75, 
    width = 50, 
    height = 5,
    points = 7,
    adjustments = [(10,-5),(-2,-2),(3,5),(-10,-5),(0,3)],
    debug = False
)

#show_object(ex_ruin)

cq.exporters.export(ex_ruin, 'stl/ruin_ruin_rectangle.stl')
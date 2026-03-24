import cadquery as cq
from cqterrain.ruin import rectangle

ex_base = rectangle(
    length = 75, 
    width = 50, 
    height = 5    
)

#show_object(ex_base)

cq.exporters.export(ex_base, 'stl/ruin_rectangle.stl')
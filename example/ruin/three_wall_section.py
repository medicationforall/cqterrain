import cadquery as cq
from cqterrain.ruin import three_wall_section

ex_base = three_wall_section(
    length = 50, 
    width = 50, 
    height = 50, 
    wall_width = 5  
)

#show_object(ex_base)

cq.exporters.export(ex_base, 'stl/ruin_three_wall_section.stl')
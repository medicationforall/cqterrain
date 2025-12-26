import cadquery as cq
from cqterrain.ruin import corner

result = corner(
    length=50, 
    width=50, 
    height=5  
)

#show_object(result)
cq.exporters.export(result, 'stl/ruin_corner.stl')
import cadquery as cq
from cqterrain import roof

result = roof.hip(
    length = 40, 
    width = 40, 
    top = 0, 
    left = 0, 
    right = 0, 
    height = 40
)

#show_object(result)
cq.exporters.export(result,'stl/roof_hip.stl')
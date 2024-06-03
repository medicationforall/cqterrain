import cadquery as cq
from cqterrain import roof

result = roof.gable(
    length = 40, 
    width = 40, 
    height = 40
)

#show_object(result)
cq.exporters.export(result,'stl/roof_gable.stl')
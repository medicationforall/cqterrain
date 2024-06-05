import cadquery as cq
from cqterrain import support

result = support(
    length = 10, 
    width = 10, 
    height = 30, 
    inner_height = 8, 
    inner_length = 4, 
    inner_width = 4, 
    top_offset = 0
)

#show_object(result)
cq.exporters.export(result,'stl/support.stl')

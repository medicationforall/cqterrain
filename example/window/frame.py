import cadquery as cq
from cqterrain import window

result = window.frame(
    length = 20, 
    width = 4, 
    height = 40, 
    frame_width = 3
)

#show_object(result)
cq.exporters.export(result,'stl/window_frame.stl')
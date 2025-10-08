import cadquery as cq
from cqterrain import pipe

ex_platform = pipe.platform(
    top_length = 42, 
    stair_y_distance = 23,
    straight_pipe= None,
    render_hollow = True,
    render_through_hole = True
)

#show_object(ex_platform)
cq.exporters.export(ex_platform,"stl/pipe_platform_pipe.stl")
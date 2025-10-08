import cadquery as cq
from cqterrain import pipe

pipe_line = pipe.straight(
    length = 75, 
    connector_length=2, 
    connector_radius = 11.5,
    render_hollow=False,
    render_through_hole=False
)

pipe_line_hollow = pipe.straight(
    length = 75, 
    connector_length=2, 
    connector_radius = 11.5,
    render_hollow=True,
    render_through_hole=True
)

#show_object(pipe_line)
cq.exporters.export(pipe_line,"stl/pipe_straight.stl")
cq.exporters.export(pipe_line_hollow,"stl/pipe_line_hollow.stl")